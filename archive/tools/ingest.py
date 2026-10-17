#!/usr/bin/env python3
"""
AI Video Prompt & Reference Archive Ingest Script
- Compresses video to 480p (H.264, web-optimized faststart)
- Generates poster thumbnail (WebP/JPG)
- Organizes reference images and prompt files
- Updates data/index.json for the web dashboard
"""

import os
import sys
import json
import shutil
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INBOX_DIR = BASE_DIR / "inbox"
DATA_DIR = BASE_DIR / "data"
INDEX_FILE = DATA_DIR / "index.json"

def run_cmd(cmd):
    """Run shell command and return stdout."""
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[Error] Command failed: {cmd}\n{res.stderr}", file=sys.stderr)
    return res.returncode == 0

def get_next_id():
    """Determine the next sequential project ID (e.g. 001, 002)."""
    if not INDEX_FILE.exists():
        return 1
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not data or not isinstance(data, list):
                return 1
            ids = [int(item.get("id", 0)) for item in data if str(item.get("id", "")).isdigit()]
            return max(ids) + 1 if ids else 1
    except Exception:
        return 1

def compress_to_480p(src_video: Path, dst_video: Path):
    """
    Compress video to 480p H.264 with AAC audio, faststart enabled.
    Adapts to both horizontal and vertical videos cleanly.
    """
    scale_filter = "scale='if(gte(iw,ih),-2,480)':'if(gte(iw,ih),480,-2)'"
    cmd = (
        f"ffmpeg -y -i '{src_video}' "
        f"-vf \"{scale_filter}\" "
        f"-c:v libx264 -preset medium -crf 26 "
        f"-c:a aac -b:a 128k "
        f"-movflags +faststart "
        f"'{dst_video}'"
    )
    print(f"🎬 Compressing video to 480p: {src_video.name} -> {dst_video.name}")
    return run_cmd(cmd)

from PIL import Image

def optimize_image_to_webp(src_img: Path, dst_webp: Path, quality: int = 75, max_size: int = 1600):
    """
    Compress image to WebP with 75% quality and maximum dimension capping.
    Reduces file size dramatically (typically 50-150KB) while preserving visual clarity.
    """
    try:
        with Image.open(src_img) as img:
            # Resize if overly large
            w, h = img.size
            if max(w, h) > max_size:
                scale = max_size / max(w, h)
                new_w, new_h = int(w * scale), int(h * scale)
                img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            
            # Save as WebP
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                img.save(dst_webp, "WEBP", quality=quality, method=6)
            else:
                img.convert("RGB").save(dst_webp, "WEBP", quality=quality, method=6)
        print(f"🖼️ Optimized to WebP (Q75): {src_img.name} -> {dst_webp.name}")
        return True
    except Exception as e:
        print(f"[Warn] Failed to convert {src_img} to WebP: {e}, falling back to direct copy")
        shutil.copy2(src_img, dst_webp.with_suffix(src_img.suffix))
        return False

def generate_thumbnail(src_video: Path, dst_thumb: Path, seek_sec: float = 1.0):
    """Capture a thumbnail frame at seek_sec and save as WebP 75%."""
    tmp_jpg = dst_thumb.with_suffix(".tmp.jpg")
    cmd = (
        f"ffmpeg -y -ss {seek_sec} -i '{src_video}' "
        f"-vframes 1 -q:v 2 '{tmp_jpg}'"
    )
    success = run_cmd(cmd)
    if not success or not tmp_jpg.exists():
        # Retry at 0.0s
        cmd_retry = f"ffmpeg -y -ss 0 -i '{src_video}' -vframes 1 -q:v 2 '{tmp_jpg}'"
        success = run_cmd(cmd_retry)
    
    if success and tmp_jpg.exists():
        optimize_image_to_webp(tmp_jpg, dst_thumb, quality=75)
        tmp_jpg.unlink(missing_ok=True)
        return True
    return False

def get_video_duration(src_video: Path) -> float:
    """Get video duration in seconds via ffprobe."""
    cmd = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 '{src_video}'"
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    try:
        return round(float(res.stdout.strip()), 1)
    except Exception:
        return 0.0

def ingest_folder(folder_path: Path, title: str = None, model: str = "Wan 3.0", category: str = "Commercial/Beauty"):
    """Ingest files from an inbox folder into archive/data."""
    folder_path = Path(folder_path).resolve()
    if not folder_path.exists():
        print(f"[Error] Folder not found: {folder_path}")
        return False

    # 1. Find video files
    video_exts = {".mp4", ".mov", ".webm", ".mkv", ".m4v"}
    videos = [f for f in folder_path.iterdir() if f.is_file() and f.suffix.lower() in video_exts]
    
    # 2. Find image files (refs)
    img_exts = {".jpg", ".jpeg", ".png", ".webp", ".avif"}
    images = sorted([f for f in folder_path.iterdir() if f.is_file() and f.suffix.lower() in img_exts and not f.name.startswith("thumb")])
    
    # 3. Find prompt text files
    txt_exts = {".txt", ".md"}
    prompt_files = [f for f in folder_path.iterdir() if f.is_file() and f.suffix.lower() in txt_exts and f.name != "meta.json"]

    prompt_content = ""
    if prompt_files:
        with open(prompt_files[0], "r", encoding="utf-8") as f:
            prompt_content = f.read()

    # Determine Project ID and Dir Name
    proj_id = get_next_id()
    slug = (title or folder_path.name).lower().replace(" ", "_").replace("-", "_")
    slug = "".join([c for c in slug if c.isalnum() or c == "_"])[:40]
    proj_dir_name = f"{proj_id:03d}_{slug}"
    dst_proj_dir = DATA_DIR / proj_dir_name
    dst_proj_dir.mkdir(parents=True, exist_ok=True)
    dst_refs_dir = dst_proj_dir / "refs"
    dst_refs_dir.mkdir(parents=True, exist_ok=True)

    # Process reference images (Optimize to WebP 75%)
    ref_filenames = []
    for idx, img in enumerate(images, start=1):
        target_name = f"ref_{idx:02d}_{img.stem}.webp"
        dst_webp_path = dst_refs_dir / target_name
        optimize_image_to_webp(img, dst_webp_path, quality=75)
        ref_filenames.append(f"refs/{target_name}")

    # Compress video
    video_filename = None
    duration = 0.0
    aspect_ratio = "16:9"
    if videos:
        raw_video = videos[0]
        dst_video = dst_proj_dir / "video_480p.mp4"
        if compress_to_480p(raw_video, dst_video):
            video_filename = "video_480p.mp4"
            duration = get_video_duration(dst_video)
        
        # Thumbnail (WebP 75%)
        dst_thumb = dst_proj_dir / "thumb.webp"
        generate_thumbnail(dst_video if dst_video.exists() else raw_video, dst_thumb)

    # Metadata creation
    meta_info = {
        "id": proj_id,
        "dir": proj_dir_name,
        "title": title or folder_path.name,
        "model": model,
        "category": category,
        "duration_sec": duration,
        "aspect_ratio": aspect_ratio,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "video_file": video_filename,
        "thumb_file": "thumb.webp" if (dst_proj_dir / "thumb.webp").exists() else None,
        "references": ref_filenames,
        "prompt": prompt_content.strip(),
        "tags": [model, category]
    }

    # Save meta.json
    with open(dst_proj_dir / "meta.json", "w", encoding="utf-8") as f:
        json.dump(meta_info, f, ensure_ascii=False, indent=2)

    # Update index.json
    update_index(meta_info)
    print(f"✅ Successfully ingested into: {dst_proj_dir.name}")
    return True

def update_index(new_meta):
    """Add or update an item in data/index.json."""
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    all_data = []
    if INDEX_FILE.exists():
        try:
            with open(INDEX_FILE, "r", encoding="utf-8") as f:
                all_data = json.load(f)
                if not isinstance(all_data, list):
                    all_data = []
        except Exception:
            all_data = []

    # Update if already exists, else append
    existing_idx = next((i for i, item in enumerate(all_data) if item.get("id") == new_meta["id"]), None)
    if existing_idx is not None:
        all_data[existing_idx] = new_meta
    else:
        all_data.append(new_meta)

    # Sort descending by ID (newest first)
    all_data.sort(key=lambda x: int(x.get("id", 0)), reverse=True)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest video & prompts into archive")
    parser.add_argument("--folder", type=str, help="Specific folder inside inbox or path to ingest")
    parser.add_argument("--title", type=str, help="Project title")
    parser.add_argument("--model", type=str, default="Wan 3.0", help="AI Model name (e.g. Wan 3.0, Kling, MiniMax)")
    parser.add_argument("--category", type=str, default="Luxury/Commercial", help="Category (e.g. Beauty, Action, MV)")
    args = parser.parse_args()

    target = Path(args.folder) if args.folder else None
    if not target or not target.exists():
        # Check if files exist directly in INBOX_DIR
        video_exts = {".mp4", ".mov", ".webm", ".mkv", ".m4v"}
        root_videos = [f for f in INBOX_DIR.iterdir() if f.is_file() and f.suffix.lower() in video_exts]
        root_images = [f for f in INBOX_DIR.iterdir() if f.is_file() and f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}]
        
        if root_videos or root_images:
            print("📦 Found files directly in inbox. Processing root inbox...")
            # Use root video stem or default as title
            detected_title = args.title or (root_videos[0].stem if root_videos else "Inbox Project")
            ingest_folder(INBOX_DIR, title=detected_title, model=args.model, category=args.category)
        else:
            # Check inbox subfolders
            subfolders = [f for f in INBOX_DIR.iterdir() if f.is_dir()]
            if not subfolders:
                print("ℹ️ No folders or files found in archive/inbox. Ready for new inputs!")
                sys.exit(0)
            for folder in subfolders:
                print(f"📦 Processing inbox folder: {folder.name}")
                ingest_folder(folder, title=args.title, model=args.model, category=args.category)
    else:
        ingest_folder(target, title=args.title, model=args.model, category=args.category)

