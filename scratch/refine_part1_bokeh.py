import cv2
import numpy as np
import os

def refine_bokeh(image_path="scratch/test_preview/part1_frame_7s.jpg", 
                 depth_path="scratch/test_preview/depth_map_7s.jpg",
                 output_dir="scratch/test_preview"):
    
    bgr = cv2.imread(image_path)
    depth = cv2.imread(depth_path, cv2.IMREAD_GRAYSCALE).astype(np.float32) / 255.0
    h, w = bgr.shape[:2]
    
    # K is ~0.8-1.0, V is ~0.35-0.55, Background is < 0.25.
    # We want BOTH K and V to be razor sharp (in focus).
    # Background (< 0.25) should be heavily blurred into creamy bokeh.
    
    # Smooth step transition: 0.0 at depth >= 0.30 (both actors sharp), 1.0 at depth <= 0.18 (background)
    bg_thresh_high = 0.30
    bg_thresh_low = 0.16
    
    blur_weight = np.clip((bg_thresh_high - depth) / (bg_thresh_high - bg_thresh_low), 0.0, 1.0)
    
    # Refine mask edge using guided filter / bilateral to respect actor hair and silhouette boundaries
    blur_weight_smooth = cv2.GaussianBlur(blur_weight, (11, 11), 0)
    
    # 1. Create Creamy Cinematic Bokeh (Multi-pass lens blur)
    # Background blur radius: 65px (large f/1.2 wide aperture circle of confusion)
    blurred_bg = cv2.GaussianBlur(bgr, (65, 65), 30)
    
    # 2. Warm Vintage Color Grade on background (removes modern sterile white ceiling)
    # Boost warm amber tone on the blurred background to match 1970s film look
    bg_vintage = blurred_bg.copy().astype(np.float32)
    bg_vintage[:, :, 0] *= 0.82 # Reduce cool blue
    bg_vintage[:, :, 1] *= 0.95 # Slightly soften green
    bg_vintage[:, :, 2] *= 1.10 # Boost warm golden/amber
    bg_vintage = np.clip(bg_vintage, 0, 255).astype(np.uint8)
    
    # 3. Composite Sharp Foreground (K & V) + Creamy Vintage Bokeh Background
    w_3c = np.repeat(blur_weight_smooth[:, :, np.newaxis], 3, axis=2)
    result = (bgr * (1.0 - w_3c) + bg_vintage * w_3c).astype(np.uint8)
    
    # Save results
    cv2.imwrite(os.path.join(output_dir, "perfect_part1_bokeh_7s.jpg"), result)
    
    comparison = np.hstack([bgr, result])
    cv2.imwrite(os.path.join(output_dir, "perfect_comparison_7s.jpg"), comparison)
    print("Refined bokeh saved successfully!")

if __name__ == "__main__":
    refine_bokeh()
