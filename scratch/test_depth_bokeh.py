import cv2
import torch
import numpy as np
import os
from transformers import AutoImageProcessor, AutoModelForDepthEstimation
from PIL import Image

def process_single_frame(image_path, output_dir="scratch/test_preview"):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Load image
    bgr_img = cv2.imread(image_path)
    h, w = bgr_img.shape[:2]
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_img)
    
    # 2. Load Depth Anything V2
    print("Loading Depth Anything V2 model...")
    checkpoint = "depth-anything/Depth-Anything-V2-Small-hf"
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    print(f"Device: {device}")
    
    processor = AutoImageProcessor.from_pretrained(checkpoint)
    model = AutoModelForDepthEstimation.from_pretrained(checkpoint).to(device)
    model.eval()
    
    # 3. Predict Depth
    inputs = processor(images=pil_img, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        post_processed_depth = processor.post_process_depth_estimation(outputs, target_sizes=[(h, w)])
    
    depth = post_processed_depth[0]["predicted_depth"].cpu().numpy()
    
    # Normalize depth (0=far, 1=near, or vice versa)
    d_min, d_max = depth.min(), depth.max()
    depth_norm = (depth - d_min) / (d_max - d_min) # 0 to 1. Closer objects usually have higher values.
    
    # Save normalized depth map visualization
    depth_vis = (depth_norm * 255).astype(np.uint8)
    cv2.imwrite(os.path.join(output_dir, "depth_map.jpg"), depth_vis)
    print("Depth map saved.")
    
    # 4. Realistic Cinematic Lens Blur (Bokeh simulation based on focal plane)
    # The mermaid protagonist is in the foreground (highest depth values).
    # Let focal plane be around the mermaid (depth ~ 0.7 to 1.0).
    # Background (warriors, arches) are at depth < 0.6.
    
    # Calculate circle of confusion (CoC) / blur weight based on distance from focal plane
    focal_depth = 0.85 # Focus locked on the mermaid
    dof_range = 0.15   # Sharp depth of field band
    
    # Blur intensity map: 0 at focal plane, increasing to 1 at background
    blur_weight = np.clip((focal_depth - depth_norm - dof_range) / 0.5, 0.0, 1.0)
    # Smooth the mask slightly to avoid harsh boundary artifacts
    blur_weight = cv2.GaussianBlur(blur_weight, (21, 21), 0)
    
    # Multi-scale bokeh blur for realistic lens blur (creamy bokeh)
    # Large blur for distant background, medium for midground
    blur_large = cv2.GaussianBlur(bgr_img, (51, 51), 25)
    # Add slight chromatic highlight boost to blurred areas for vintage lens feel
    
    # Blend sharp and blurred based on 3D depth map
    # 3-channel weight
    weight_3c = np.repeat(blur_weight[:, :, np.newaxis], 3, axis=2)
    bokeh_result = (bgr_img * (1.0 - weight_3c) + blur_large * weight_3c).astype(np.uint8)
    
    # Save comparison image (side-by-side)
    cv2.imwrite(os.path.join(output_dir, "bokeh_result.jpg"), bokeh_result)
    
    # Side-by-side comparison
    comparison = np.hstack([bgr_img, bokeh_result])
    cv2.imwrite(os.path.join(output_dir, "comparison_before_after.jpg"), comparison)
    print("Bokeh rendering complete! Saved to scratch/test_preview/bokeh_result.jpg and comparison_before_after.jpg")

if __name__ == "__main__":
    process_single_frame("scratch/test_preview/frame_2s.jpg")
