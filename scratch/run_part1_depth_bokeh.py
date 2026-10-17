import cv2
import torch
import numpy as np
import os
from transformers import AutoImageProcessor, AutoModelForDepthEstimation
from PIL import Image

def process_depth_bokeh(input_img_path, output_dir="scratch/test_preview"):
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Load Image
    bgr = cv2.imread(input_img_path)
    h, w = bgr.shape[:2]
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb)
    
    # 2. Depth Anything V2 Inference
    print("Loading Depth Anything V2...")
    checkpoint = "depth-anything/Depth-Anything-V2-Small-hf"
    device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    
    processor = AutoImageProcessor.from_pretrained(checkpoint)
    model = AutoModelForDepthEstimation.from_pretrained(checkpoint).to(device)
    model.eval()
    
    inputs = processor(images=pil_img, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model(**inputs)
        post_processed_depth = processor.post_process_depth_estimation(outputs, target_sizes=[(h, w)])
    
    depth = post_processed_depth[0]["predicted_depth"].cpu().numpy()
    
    # Normalize 0.0 ~ 1.0 (Higher = closer to camera)
    d_min, d_max = depth.min(), depth.max()
    depth_norm = (depth - d_min) / (d_max - d_min)
    
    # Save Depth Map Image
    depth_vis = (depth_norm * 255).astype(np.uint8)
    cv2.imwrite(os.path.join(output_dir, "depth_map_7s.jpg"), depth_vis)
    print("Depth map generated.")
    
    # 3. Cinematic Physical Lens Blur & Creamy Bokeh
    # Foreground actors (K & V) are in the closest range (depth > 0.6).
    # Background (ceiling, white track lights, distant windows) is at depth < 0.5.
    
    # Threshold & gradient for focus transition
    # Focal plane is locked on the two killers (depth ~ 0.6 to 1.0)
    focus_cutoff = 0.55
    transition_width = 0.15
    
    # Blur weight: 0.0 at foreground (sharp), 1.0 at distant background (blurred)
    blur_weight = np.clip((focus_cutoff - depth_norm) / transition_width, 0.0, 1.0)
    
    # Feather the edge with bilateral / guided filter to preserve sharp hair & mask boundaries
    blur_weight_smooth = cv2.GaussianBlur(blur_weight, (15, 15), 0)
    
    # Multi-pass realistic optical bokeh (large radius blur simulating f/1.2 wide aperture)
    # Background blur radius: 55px
    blurred_bg = cv2.GaussianBlur(bgr, (55, 55), 25)
    
    # Extra warmth and highlight glow on blurred background (vintage cinema halation look)
    # Slight golden tint to the blurred background
    blurred_bg_tinted = blurred_bg.copy().astype(np.float32)
    blurred_bg_tinted[:, :, 0] *= 0.90 # slight blue drop
    blurred_bg_tinted[:, :, 2] *= 1.05 # slight red/warm boost
    blurred_bg_tinted = np.clip(blurred_bg_tinted, 0, 255).astype(np.uint8)
    
    # Composite foreground (sharp original) + background (creamy bokeh)
    w_3c = np.repeat(blur_weight_smooth[:, :, np.newaxis], 3, axis=2)
    final_bokeh = (bgr * (1.0 - w_3c) + blurred_bg_tinted * w_3c).astype(np.uint8)
    
    cv2.imwrite(os.path.join(output_dir, "part1_bokeh_7s.jpg"), final_bokeh)
    
    # Side-by-side comparison (Before vs After)
    comparison = np.hstack([bgr, final_bokeh])
    cv2.imwrite(os.path.join(output_dir, "part1_comparison_7s.jpg"), comparison)
    print("Done! Result saved to scratch/test_preview/part1_bokeh_7s.jpg and part1_comparison_7s.jpg")

if __name__ == "__main__":
    process_depth_bokeh("scratch/test_preview/part1_frame_7s.jpg")
