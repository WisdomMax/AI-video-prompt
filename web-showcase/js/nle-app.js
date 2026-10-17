// NLE Timeline Studio App Engine
document.addEventListener("DOMContentLoaded", () => {
  let currentProject = SKILLS_DATA[0];
  let currentShotIndex = 0;
  let isPlaying = false;
  let playInterval = null;

  // DOM Elements
  const projectSelect = document.getElementById("project-select");
  const binItems = document.getElementById("bin-items");
  const timecodeDisplay = document.getElementById("timecode-display");
  const playBtn = document.getElementById("play-btn");
  const playheadLine = document.getElementById("playhead-line");
  const copyMasterBtn = document.getElementById("copy-master-btn");
  const toastBar = document.getElementById("toast-bar");

  // Monitor elements
  const visualIcon = document.getElementById("visual-icon");
  const visualTitle = document.getElementById("visual-title");
  const visualDetail = document.getElementById("visual-detail");
  const shotBadge = document.getElementById("shot-badge");
  const monitorRes = document.getElementById("monitor-res");
  const monitorFps = document.getElementById("monitor-fps");

  // Inspector elements
  const inspectorTitle = document.getElementById("inspector-title");
  const inspectorModel = document.getElementById("inspector-model");
  const inspectorRatio = document.getElementById("inspector-ratio");
  const inspectorDuration = document.getElementById("inspector-duration");
  const promptTextarea = document.getElementById("prompt-textarea");
  const charCounter = document.getElementById("char-counter");
  const copyPromptBtn = document.getElementById("copy-prompt-btn");

  // Tracks elements
  const trackVideo = document.getElementById("track-video");
  const trackFx = document.getElementById("track-fx");
  const trackAudio = document.getElementById("track-audio");
  const rulerMarks = document.getElementById("ruler-marks");

  // Populate project selector & bin items
  function initProjects() {
    projectSelect.innerHTML = "";
    binItems.innerHTML = "";

    SKILLS_DATA.forEach((skill, idx) => {
      // Option
      const opt = document.createElement("option");
      opt.value = skill.id;
      opt.textContent = `[${skill.tag}] ${skill.title}`;
      projectSelect.appendChild(opt);

      // Bin item
      const item = document.createElement("div");
      item.className = `bin-item ${idx === 0 ? "active" : ""}`;
      item.dataset.id = skill.id;
      item.innerHTML = `
        <div class="bin-item-tag">${skill.tag} · ${skill.duration}</div>
        <div class="bin-item-title">${skill.title}</div>
        <div class="bin-item-meta">${skill.aspectRatio} · ${skill.timeline.length} Shots</div>
      `;

      item.addEventListener("click", () => {
        selectProject(skill.id);
      });

      binItems.appendChild(item);
    });

    projectSelect.addEventListener("change", (e) => {
      selectProject(e.target.value);
    });
  }

  // Select project
  function selectProject(id) {
    currentProject = SKILLS_DATA.find(s => s.id === id);
    currentShotIndex = 0;
    projectSelect.value = id;

    // Update bin active state
    document.querySelectorAll(".bin-item").forEach(item => {
      item.classList.toggle("active", item.dataset.id === id);
    });

    // Update Inspector
    inspectorTitle.textContent = currentProject.title;
    inspectorModel.textContent = currentProject.model;
    inspectorRatio.textContent = currentProject.aspectRatio;
    inspectorDuration.textContent = currentProject.duration;
    promptTextarea.value = currentProject.prompt;
    charCounter.textContent = `${currentProject.prompt.length} chars (Limit: 2,000 ~ 2,450)`;

    // Update Monitor specs
    monitorRes.textContent = `${currentProject.aspectRatio} 2K REC.709`;
    monitorFps.textContent = `24.00 FPS · ${currentProject.duration}`;

    // Render Timeline Clips
    renderTimeline();

    // Set first shot
    setShot(0);
  }

  // Render Timeline Multi-Tracks
  function renderTimeline() {
    trackVideo.innerHTML = "";
    trackFx.innerHTML = "";
    trackAudio.innerHTML = "";

    const shots = currentProject.timeline;
    const shotCount = shots.length;

    shots.forEach((shot, idx) => {
      // V1: Video Clip
      const vClip = document.createElement("div");
      vClip.className = `clip-block clip-v1 ${idx === currentShotIndex ? "active" : ""}`;
      vClip.style.flex = "1";
      vClip.innerHTML = `
        <div class="clip-title">Shot ${idx + 1}: ${shot.label}</div>
        <div class="clip-meta">${shot.time}</div>
      `;
      vClip.addEventListener("click", () => setShot(idx));
      trackVideo.appendChild(vClip);

      // V2: Motion/FX Clip
      const fxClip = document.createElement("div");
      fxClip.className = "clip-block clip-v2";
      fxClip.style.flex = "1";
      fxClip.innerHTML = `
        <div class="clip-title">FX: ${shot.label} Dynamic</div>
        <div class="clip-meta">Keyframe Sync</div>
      `;
      trackFx.appendChild(fxClip);

      // A1: Native Audio/Foley
      const aClip = document.createElement("div");
      aClip.className = "clip-block clip-a1";
      aClip.style.flex = "1";
      aClip.innerHTML = `
        <div class="clip-title">Audio: Foley & Voice Track</div>
        <div class="clip-meta">Sync 1:1</div>
      `;
      trackAudio.appendChild(aClip);
    });
  }

  // Set active shot & update monitor
  function setShot(idx) {
    currentShotIndex = idx;
    const shot = currentProject.timeline[idx];
    if (!shot) return;

    // Update active clip styling
    const clips = trackVideo.querySelectorAll(".clip-block");
    clips.forEach((c, i) => {
      c.classList.toggle("active", i === idx);
    });

    // Update Monitor
    visualTitle.textContent = shot.label;
    visualDetail.textContent = shot.detail;
    shotBadge.textContent = `CUT 0${idx + 1} · ${shot.time}`;
    visualIcon.textContent = currentProject.visualIcon;

    // Update Timecode
    timecodeDisplay.textContent = `00:00:0${idx * 2}:00`;

    // Move Playhead line
    const totalClips = currentProject.timeline.length;
    const trackWidth = trackVideo.clientWidth;
    const clipWidth = trackWidth / totalClips;
    const leftPos = 120 + (idx * clipWidth) + (clipWidth / 2);
    playheadLine.style.left = `${leftPos}px`;
  }

  // Playhead transport play/pause simulation
  function togglePlay() {
    isPlaying = !isPlaying;
    playBtn.textContent = isPlaying ? "⏸" : "▶";

    if (isPlaying) {
      playInterval = setInterval(() => {
        let nextIdx = (currentShotIndex + 1) % currentProject.timeline.length;
        setShot(nextIdx);
      }, 1600);
    } else {
      clearInterval(playInterval);
    }
  }

  playBtn.addEventListener("click", togglePlay);

  // Copy helpers
  function copyText(text, msg) {
    navigator.clipboard.writeText(text);
    toastBar.textContent = msg;
    toastBar.classList.add("show");
    setTimeout(() => {
      toastBar.classList.remove("show");
    }, 2200);
  }

  copyPromptBtn.addEventListener("click", () => {
    copyText(promptTextarea.value, "📋 프로덕션 마스터 프롬프트 복사 완료!");
  });

  copyMasterBtn.addEventListener("click", () => {
    copyText(promptTextarea.value, "📋 마스터 프롬프트가 클립보드에 복사되었습니다!");
  });

  // Hotkeys (Space: Play/Pause, Left/Right: Shot Nav)
  window.addEventListener("keydown", (e) => {
    if (e.target.tagName === "TEXTAREA" || e.target.tagName === "INPUT") return;
    if (e.code === "Space") {
      e.preventDefault();
      togglePlay();
    } else if (e.code === "ArrowRight") {
      e.preventDefault();
      let next = (currentShotIndex + 1) % currentProject.timeline.length;
      setShot(next);
    } else if (e.code === "ArrowLeft") {
      e.preventDefault();
      let prev = (currentShotIndex - 1 + currentProject.timeline.length) % currentProject.timeline.length;
      setShot(prev);
    }
  });

  // Init
  initProjects();
  selectProject(SKILLS_DATA[0].id);
});
