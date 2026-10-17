import cv2
import numpy as np
import os

def create_natural_bokeh_levels(image_path="scratch/test_preview/part1_frame_7s.jpg", 
                               depth_path="scratch/test_preview/depth_map_7s.jpg",
                               output_dir="scratch/test_preview"):
    
    bgr = cv2.imread(image_path)
    depth = cv2.imread(depth_path, cv2.IMREAD_GRAYSCALE).astype(np.float32) / 255.0
    h, w = bgr.shape[:2]
    
    # K: ~0.8-1.0, V: ~0.35-0.55, Background: < 0.25
    # Smooth step transition strictly focusing on distant background only
    # bg_thresh: 0.25 to 0.12 (even further back, so V is 100% safe)
    bg_thresh_high = 0.26
    bg_thresh_low = 0.12
    
    raw_mask = np.clip((bg_thresh_high - depth) / (bg_thresh_high - bg_thresh_low), 0.0, 1.0)
    
    # To prevent halo bleeding around actor silhouettes, erode the blur mask slightly into background
    kernel = np.ones((5, 5), np.uint8)
    eroded_mask = cv2.erode((raw_mask * 255).astype(np.uint8), kernel, iterations=1).astype(np.float32) / 255.0
    smooth_mask = cv2.GaussianBlur(eroded_mask, (7, 7), 0)
    mask_3c = np.repeat(smooth_mask[:, :, np.newaxis], 3, axis=2)
    
    levels = {
        "Level_1_f2.8_Subtle": (15, 5),    # 아주 자연스러운 미세 심도 (15px)
        "Level_2_f2.0_Moderate": (25, 10),  # 적당히 부드러운 심도 (25px)
        "Level_3_f1.8_Soft": (37, 15),      # 소프트한 심도 (37px)
    }
    
    results = [bgr] # Start with original
    
    for name, (ksize, sigma) in levels.items():
        # Lens blur without arbitrary color shift (keep original color & ambient light 100% intact!)
        blurred = cv2.GaussianBlur(bgr, (ksize, ksize), sigma)
        
        # Natural composite: sharp foreground + mildly softened background
        comp = (bgr * (1.0 - mask_3c) + blurred * mask_3c).astype(np.uint8)
        
        # Add subtle film grain over entire image to unify texture and eliminate any synthetic digital look
        grain = np.random.normal(0, 2.5, comp.shape).astype(np.float32)
        comp_with_grain = np.clip(comp.astype(np.float32) + grain, 0, 255).astype(np.uint8)
        
        results.append(comp_with_grain)
        cv2.imwrite(os.path.join(output_dir, f"{name}.jpg"), comp_with_grain)
    
    # Create side-by-side comparison of all 4: Original, Level 1, Level 2, Level 3
    # Resize width to fit comfortably in inspection
    scaled = [cv2.resize(img, (int(w * 0.5), int(h * 0.5))) for img in results]
    
    # Put labels on them
    labels = ["ORIGINAL (Pan-focus)", "LEVEL 1 (f/2.8 Subtle)", "LEVEL 2 (f/2.0 Moderate)", "LEVEL 3 (f/1.8 Soft)"]
    for img, label in zip(scaled, labels):
        cv2.rectangle(img, (0, 0), (img.shape[1], 45), (0, 0, 0), -1)
        cv2.putText(img, label, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
        
    grid = np.hstack(scaled)
    cv2.imwrite(os.path.join(output_dir, "bokeh_intensity_comparison.jpg"), grid)
    print("Generated natural bokeh levels successfully!")

if __name__ == "__main__":
    create_natural_bokeh_levels()
