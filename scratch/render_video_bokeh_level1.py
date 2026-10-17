import cv2
import torch
import numpy as np
import os
import subprocess
import time
from transformers import AutoImageProcessor, AutoModelForDepthEstimation
from PIL import Image

def process_video_level_1(input_video="production/sheets/1.mp4", 
                          output_video="production/sheets/1_cinematic_bokeh_level1.mp4",
                          batch_size=4):
    
    if not os.path.exists(input_video):
        print(f"Error: {input_video} not found!")
        return

    temp_video = "scratch/temp_1_bokeh_level1_video.mp4"
    os.makedirs("scratch", exist_ok=True)
    
    cap = cv2.VideoCapture(input_video)
    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(f"Input: {input_video} | {width}x{height} | {fps:.2f} FPS | Total: {total_frames} frames")
    
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    print(f"Using device: {device}")
    
    checkpoint = "depth-anything/Depth-Anything-V2-Small-hf"
    processor = AutoImageProcessor.from_pretrained(checkpoint)
    model = AutoModelForDepthEstimation.from_pretrained(checkpoint).to(device)
    model.eval()
    
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(temp_video, fourcc, fps, (width, height))
    
    # Erode kernel for actor silhouette boundary preservation (Zero halo, Zero bleeding)
    kernel = np.ones((5, 5), np.uint8)
    
    # LEVEL 1 Tuning parameters (Ultra-Natural f/2.8 Subtle - ZERO halo, perfectly transparent)
    bg_thresh_high = 0.26
    bg_thresh_low = 0.12
    ksize = 15   # Level 1 Subtle
    sigma = 5.0  # Level 1 Subtle
    
    frame_idx = 0
    start_time = time.time()
    
    batch_frames = []
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        batch_frames.append(frame)
        
        if len(batch_frames) == batch_size or (frame_idx + len(batch_frames) == total_frames):
            pil_images = [Image.fromarray(cv2.cvtColor(f, cv2.COLOR_BGR2RGB)) for f in batch_frames]
            inputs = processor(images=pil_images, return_tensors="pt").to(device)
            
            with torch.no_grad():
                outputs = model(**inputs)
                post_depths = processor.post_process_depth_estimation(outputs, target_sizes=[(height, width)] * len(batch_frames))
            
            for bgr, depth_dict in zip(batch_frames, post_depths):
                depth = depth_dict["predicted_depth"].cpu().numpy()
                d_min, d_max = depth.min(), depth.max()
                depth_norm = (depth - d_min) / (d_max - d_min + 1e-8)
                
                # Mask generation: actor area = 0.0 (100% original untouched pixels), background = 1.0
                raw_mask = np.clip((bg_thresh_high - depth_norm) / (bg_thresh_high - bg_thresh_low), 0.0, 1.0)
                eroded_mask = cv2.erode((raw_mask * 255).astype(np.uint8), kernel, iterations=1).astype(np.float32) / 255.0
                smooth_mask = cv2.GaussianBlur(eroded_mask, (7, 7), 0)
                mask_3c = np.repeat(smooth_mask[:, :, np.newaxis], 3, axis=2)
                
                # Level 1 Ultra-Mild Lens Blur ONLY on the distant background
                blurred_bg = cv2.GaussianBlur(bgr, (ksize, ksize), sigma)
                
                # Composite: Actor retains 100% original raw pixel data, background softened at Level 1
                final_frame = (bgr * (1.0 - mask_3c) + blurred_bg * mask_3c).astype(np.uint8)
                
                # Zero added artificial grain / zero color distortion to preserve pristine original quality
                out.write(final_frame)
                frame_idx += 1
                
                if frame_idx % 30 == 0 or frame_idx == total_frames:
                    elapsed = time.time() - start_time
                    fps_proc = frame_idx / elapsed
                    remaining = (total_frames - frame_idx) / fps_proc if fps_proc > 0 else 0
                    print(f"Rendered [{frame_idx}/{total_frames}] frames ({frame_idx/total_frames*100:.1f}%) | Speed: {fps_proc:.1f} fps | ETA: {remaining:.1f}s")
                    
            batch_frames = []
            
    cap.release()
    out.release()
    print("Video frame processing completed.")
    
    # Merge with original audio stream without quality loss (-c:a copy, -crf 15 for near-lossless video)
    print("Final high-fidelity ffmpeg muxing...")
    cmd = [
        "ffmpeg", "-y",
        "-i", temp_video,
        "-i", input_video,
        "-c:v", "libx264", "-crf", "15", "-preset", "slow",
        "-pix_fmt", "yuv420p",
        "-map", "0:v:0",
        "-map", "1:a:0?",
        "-c:a", "copy",
        output_video
    ]
    
    subprocess.run(cmd, check=True)
    if os.path.exists(temp_video):
        os.remove(temp_video)
        
    print(f"🎉 Final processed video successfully saved to: {output_video}")

if __name__ == "__main__":
    process_video_level_1()
