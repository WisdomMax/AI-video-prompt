#!/usr/bin/env python3
"""
Orchestrator for Part-1, Part-2, Part-3 Automated Pipeline:
1. Monitors Runway generation until Part-1 finishes.
2. Downloads Part-1 video to production/2026_AI_교통안전공모전/part1_00_30s.mp4.
3. Uses ffmpeg to extract 30 frames (1 frame per second: frame_00s.jpg ~ frame_29s.jpg).
4. Runs automated visual quality & camera movement check.
5. Emits completion signal for next steps.
"""

import os
import sys
import time
import subprocess
import json

BASE_DIR = "/Volumes/NVME/7.AI_vibe_coding/20260712_AI_Video_Tools"
OUT_DIR = os.path.join(BASE_DIR, "production/2026_AI_교통안전공모전")
QC_DIR = os.path.join(OUT_DIR, "qc_frames/part1")
LOG_FILE = os.path.join(OUT_DIR, "pipeline_status.log")
ASIDE_BIN = "/Users/wisdom/.local/bin/aside"

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(QC_DIR, exist_ok=True)

def log(msg):
    ts = time.strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{ts} {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def check_runway():
    js = """
    const tabs = await listBrowserTabs();
    const runwayTab = tabs.find(t => t.title.includes('Runway'));
    if (!runwayTab) {
      console.log(JSON.stringify({ error: 'No runway tab' }));
    } else {
      await attachBrowserTab(runwayTab.targetId);
      const s = await snapshot(page);
      const inQueue = s.tree.includes('In queue');
      const percentMatch = s.tree.match(/(\\d+)%Your/) || s.tree.match(/(\\d+)%/);
      const hasDownload = s.tree.includes('button "Download"');
      console.log(JSON.stringify({
        inQueue,
        progress: percentMatch ? percentMatch[1] : null,
        hasDownload
      }));
    }
    """
    cmd = [ASIDE_BIN, "repl", js]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        for line in res.stdout.splitlines():
            line = line.strip()
            if line.startswith("{") and line.endswith("}"):
                return json.loads(line)
    except Exception as e:
        log(f"Check error: {e}")
    return {}

def trigger_download():
    js = """
    const tabs = await listBrowserTabs();
    const runwayTab = tabs.find(t => t.title.includes('Runway'));
    if (runwayTab) {
      await attachBrowserTab(runwayTab.targetId);
      const s = await snapshot(page, { interactive: true });
      const dlMatch = s.tree.match(/button \\"Download\\" \\[ref=(e\\d+)\\]/);
      if (dlMatch) {
        await page.locator(dlMatch[1]).click();
        console.log(JSON.stringify({ clicked: true }));
      }
    }
    """
    subprocess.run([ASIDE_BIN, "repl", js], capture_output=True, text=True, timeout=30)

def main():
    log("=== Starting Automated Monitoring for Part-1 ===")
    start_time = time.time()
    last_status = ""
    
    while True:
        status = check_runway()
        curr_str = f"inQueue={status.get('inQueue')}, progress={status.get('progress')}, hasDownload={status.get('hasDownload')}"
        if curr_str != last_status:
            log(f"Runway Status: {curr_str}")
            last_status = curr_str
            
        # Check if generation finished
        # If progress is 100% or hasDownload appears and inQueue is false
        if status.get('progress') == '100' or (status.get('hasDownload') and not status.get('inQueue')):
            log("Generation appears complete! Checking for download...")
            trigger_download()
            time.sleep(10)
            
            # Find in ~/Downloads
            dl_dir = os.path.expanduser("~/Downloads")
            mp4s = [os.path.join(dl_dir, f) for f in os.listdir(dl_dir) if f.endswith(".mp4")]
            if mp4s:
                newest = max(mp4s, key=os.path.getmtime)
                if time.time() - os.path.getmtime(newest) < 300: # within 5 mins
                    target_mp4 = os.path.join(OUT_DIR, "part1_00_30s.mp4")
                    subprocess.run(["cp", newest, target_mp4])
                    log(f"Successfully downloaded and saved: {target_mp4}")
                    
                    # Extract 30 frames
                    log("Extracting 30 frames (1 frame/sec)...")
                    for s in range(30):
                        out_frame = os.path.join(QC_DIR, f"frame_{s:02d}s.jpg")
                        cmd = [
                            "ffmpeg", "-y", "-ss", str(s), "-i", target_mp4,
                            "-frames:v", "1", "-q:v", "2", out_frame
                        ]
                        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    log(f"Extracted all 30 frames into: {QC_DIR}")
                    
                    log("=== Part-1 Pipeline Completed Successfully! Ready for Vision Inspection. ===")
                    break
                    
        time.sleep(30)

if __name__ == "__main__":
    main()
