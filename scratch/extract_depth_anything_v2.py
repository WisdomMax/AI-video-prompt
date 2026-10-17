import cv2
import torch
import numpy as np
import os
import sys
from tqdm import tqdm
from transformers import AutoImageProcessor, AutoModelForDepthEstimation
from PIL import Image

def main(video_path, output_dir="output_depth_anything"):
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        return

    os.makedirs(output_dir, exist_ok=True)
    depth_dir = os.path.join(output_dir, "depth")
    os.makedirs(depth_dir, exist_ok=True)

    # 1. Initialize Video Reader
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Processing: {video_path} ({width}x{height}, {fps} FPS, {total_frames} frames)")

    # 2. Initialize Depth Anything v2 Model (Small version for speed and sharp quality)
    print("Loading Depth Anything v2 (small) model from Hugging Face...")
    checkpoint = "depth-anything/Depth-Anything-V2-Small-hf"
    
    # Use MPS (Metal) on Mac if available, else CPU
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    print(f"Using device: {device}")
    
    image_processor = AutoImageProcessor.from_pretrained(checkpoint)
    model = AutoModelForDepthEstimation.from_pretrained(checkpoint).to(device)
    model.eval()

    # 3. Initialize Video Writer for Depth-Only Output
    temp_video_path = os.path.join(output_dir, "depth_only_temp.mp4")
    out_video = cv2.VideoWriter(
        temp_video_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (width, height)
    )

    frame_idx = 0
    with tqdm(total=total_frames, desc="Depth Anything v2 Processing") as pbar:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert BGR (OpenCV) to RGB for PIL Image processing
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(rgb_frame)

            # Preprocess image
            inputs = image_processor(images=pil_image, return_tensors="pt").to(device)

            # Model inference
            with torch.no_grad():
                outputs = model(**inputs)
                post_processed_depth = image_processor.post_process_depth_estimation(
                    outputs,
                    target_sizes=[(height, width)]
                )
            
            # Extract depth tensor and convert to numpy
            depth_map = post_processed_depth[0]["predicted_depth"].cpu().numpy()
            
            # Normalize to 0-255 range
            depth_min = depth_map.min()
            depth_max = depth_map.max()
            if depth_max - depth_min > 0:
                depth_norm = (255 * (depth_map - depth_min) / (depth_max - depth_min)).astype(np.uint8)
            else:
                depth_norm = np.zeros_like(depth_map, dtype=np.uint8)
            
            # Convert single channel to 3 channels (grayscale BGR)
            depth_bgr = cv2.cvtColor(depth_norm, cv2.COLOR_GRAY2BGR)

            # Save individual png frame
            cv2.imwrite(os.path.join(depth_dir, f"depth_{frame_idx:05d}.png"), depth_norm)

            # Write Pure Depth Frame (no original video)
            out_video.write(depth_bgr)
            
            frame_idx += 1
            pbar.update(1)

    cap.release()
    out_video.release()

    # 5. Mux Audio from Source Video using ffmpeg
    import subprocess
    final_output_path = os.path.join(output_dir, "depth_with_audio.mp4")
    print("\nMuxing audio from source video using ffmpeg...")
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-i", temp_video_path,
        "-i", video_path,
        "-map", "0:v:0",
        "-map", "1:a:0?",  # Optional: only copy audio if present
        "-c:v", "copy",
        "-c:a", "aac",
        final_output_path
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path)
        print(f"Success! Final depth video with audio created at: {final_output_path}")
    except Exception as e:
        print(f"Warning: Audio muxing failed ({e}). Outputting video without audio.")
        if os.path.exists(temp_video_path):
            os.rename(temp_video_path, final_output_path)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 extract_depth_anything_v2.py <path_to_video>")
    else:
        main(sys.argv[1])
