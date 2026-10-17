import cv2
import torch
import numpy as np
import os
import sys
from tqdm import tqdm

# Import MediaPipe solutions safely
try:
    from mediapipe.python.solutions import pose as mp_pose
    from mediapipe.python.solutions import drawing_utils as mp_drawing
    from mediapipe.python.solutions import drawing_styles as mp_drawing_styles
    HAS_MEDIAPIPE = True
except Exception as e:
    print(f"Warning: MediaPipe Pose initialization failed ({e}). Running Depth Map only.")
    HAS_MEDIAPIPE = False

def main(video_path, output_dir="output_signals"):
    global HAS_MEDIAPIPE  # Declare at the very beginning of the function
    
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    os.makedirs(output_dir, exist_ok=True)
    depth_dir = os.path.join(output_dir, "depth")
    pose_dir = os.path.join(output_dir, "pose")
    combined_dir = os.path.join(output_dir, "combined")
    os.makedirs(depth_dir, exist_ok=True)
    os.makedirs(pose_dir, exist_ok=True)
    os.makedirs(combined_dir, exist_ok=True)

    # 1. Initialize Video Reader
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Processing: {video_path} ({width}x{height}, {fps} FPS, {total_frames} frames)")

    # 2. Initialize MediaPipe Pose if available
    pose_detector = None
    if HAS_MEDIAPIPE:
        try:
            pose_detector = mp_pose.Pose(static_image_mode=False, model_complexity=1, min_detection_confidence=0.5)
        except Exception as e:
            print(f"Could not load MediaPipe Pose detector: {e}")
            HAS_MEDIAPIPE = False

    # 3. Initialize MiDaS Depth Model
    print("Loading MiDaS Depth model...")
    model_type = "DPT_Large"  # Dense Prediction Transformer (Highest quality)
    midas = torch.hub.load("intel-isl/MiDaS", model_type)
    
    # Use MPS (Metal) on Mac if available, else CPU
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    print(f"Using device: {device}")
    midas.to(device)
    midas.eval()

    midas_transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
    transform = midas_transforms.dpt_transform

    # 4. Initialize Video Writer for Combined Output (Original | Depth | Pose)
    combined_video_path = os.path.join(output_dir, "combined_preview.mp4")
    # Output width is multiplied by 3 (or 2 if MediaPipe is offline)
    cols = 3 if HAS_MEDIAPIPE else 2
    out_video = cv2.VideoWriter(
        combined_video_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width * cols, height)
    )

    frame_idx = 0
    with tqdm(total=total_frames, desc="Extracting Signals") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert BGR (OpenCV) to RGB for PyTorch/MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # --- A. Depth Map Extraction ---
            input_batch = transform(rgb_frame).to(device)
            with torch.no_grad():
                prediction = midas(input_batch)
                prediction = torch.nn.functional.interpolate(
                    prediction.unsqueeze(1),
                    size=frame.shape[:2],
                    mode="bicubic",
                    align_corners=False,
                ).squeeze()
            
            depth_map = prediction.cpu().numpy()
            # Normalize to 0-255 range for image saving
            depth_min = depth_map.min()
            depth_max = depth_map.max()
            if depth_max - depth_min > 0:
                depth_norm = (255 * (depth_map - depth_min) / (depth_max - depth_min)).astype(np.uint8)
            else:
                depth_norm = np.zeros_like(depth_map, dtype=np.uint8)
            
            # Convert single channel to 3 channels (grayscale BGR)
            depth_bgr = cv2.cvtColor(depth_norm, cv2.COLOR_GRAY2BGR)

            # --- B. Pose Skeleton Extraction ---
            pose_canvas = None
            if HAS_MEDIAPIPE and pose_detector:
                results = pose_detector.process(rgb_frame)
                pose_canvas = np.zeros_like(frame)
                if results.pose_landmarks:
                    mp_drawing.draw_landmarks(
                        pose_canvas,
                        results.pose_landmarks,
                        mp_pose.POSE_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
                    )
                cv2.imwrite(os.path.join(pose_dir, f"pose_{frame_idx:05d}.png"), pose_canvas)

            # --- C. Save Depth Frames ---
            cv2.imwrite(os.path.join(depth_dir, f"depth_{frame_idx:05d}.png"), depth_norm)

            # --- D. Write Combined Frame to Video ---
            if HAS_MEDIAPIPE:
                combined_frame = np.hstack((frame, depth_bgr, pose_canvas))
            else:
                combined_frame = np.hstack((frame, depth_bgr))
            out_video.write(combined_frame)
            
            frame_idx += 1
            pbar.update(1)

    cap.release()
    out_video.release()
    if pose_detector:
        pose_detector.close()
    print(f"\nExtraction complete!")
    print(f" - Depth Frames: {depth_dir}")
    if HAS_MEDIAPIPE:
        print(f" - Pose Frames: {pose_dir}")
    print(f" - Combined Video Preview: {combined_video_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract_depth_pose.py <path_to_video>")
    else:
        main(sys.argv[1])
