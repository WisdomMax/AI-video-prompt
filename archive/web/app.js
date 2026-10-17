/**
 * AI Video Showcase Application Logic
 */

let allProjects = [];
let currentFilterModel = 'all';
let currentSearchQuery = '';
let selectedProject = null;

// DOM Elements
const videoGrid = document.getElementById('videoGrid');
const emptyState = document.getElementById('emptyState');
const searchInput = document.getElementById('searchInput');
const searchCount = document.getElementById('searchCount');
const modelFilters = document.getElementById('modelFilters');

// Detail Modal Elements
const detailModal = document.getElementById('detailModal');
const closeModalBtn = document.getElementById('closeModalBtn');
const modalVideo = document.getElementById('modalVideo');
const modalVideoPlaceholder = document.getElementById('modalVideoPlaceholder');
const modalRefsSection = document.getElementById('modalRefsSection');
const modalRefsList = document.getElementById('modalRefsList');
const modalModelBadge = document.getElementById('modalModelBadge');
const modalCategoryBadge = document.getElementById('modalCategoryBadge');
const modalDurationBadge = document.getElementById('modalDurationBadge');
const modalAspectBadge = document.getElementById('modalAspectBadge');
const modalTitle = document.getElementById('modalTitle');
const modalDate = document.getElementById('modalDate');
const modalPrompt = document.getElementById('modalPrompt');
const copyPromptBtn = document.getElementById('copyPromptBtn');

// Inbox Guide Modal Elements
const inboxHelpBtn = document.getElementById('inboxHelpBtn');
const inboxModal = document.getElementById('inboxModal');
const closeInboxGuideBtn = document.getElementById('closeInboxGuideBtn');

// Initialize
async function init() {
  await loadProjects();
  setupEventListeners();
  renderGrid();
}

// Load data from ../data/index.json
async function loadProjects() {
  try {
    const res = await fetch('../data/index.json?t=' + Date.now());
    if (res.ok) {
      allProjects = await res.json();
    } else {
      allProjects = [];
    }
  } catch (err) {
    console.warn('No index.json found yet or error loading:', err);
    allProjects = [];
  }
}

// Setup Event Listeners
function setupEventListeners() {
  // Search
  searchInput.addEventListener('input', (e) => {
    currentSearchQuery = e.target.value.toLowerCase().trim();
    renderGrid();
  });

  // Model Filters
  modelFilters.addEventListener('click', (e) => {
    const chip = e.target.closest('.filter-chip');
    if (!chip) return;

    document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
    currentFilterModel = chip.dataset.model;
    renderGrid();
  });

  // Modal Close
  closeModalBtn.addEventListener('click', closeModal);
  detailModal.addEventListener('click', (e) => {
    if (e.target === detailModal) closeModal();
  });

  // Inbox Guide Modal
  inboxHelpBtn.addEventListener('click', () => inboxModal.classList.remove('hidden'));
  closeInboxGuideBtn.addEventListener('click', () => inboxModal.classList.add('hidden'));
  inboxModal.addEventListener('click', (e) => {
    if (e.target === inboxModal) inboxModal.classList.add('hidden');
  });

  // Copy Prompt
  copyPromptBtn.addEventListener('click', copyPromptToClipboard);

  // Keyboard Shortcuts
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeModal();
      inboxModal.classList.add('hidden');
    }
  });
}

// Filter projects
function getFilteredProjects() {
  return allProjects.filter(p => {
    // Model match
    const matchModel = currentFilterModel === 'all' || 
                       (p.model && p.model.toLowerCase().includes(currentFilterModel.toLowerCase()));

    // Search query match
    let matchQuery = true;
    if (currentSearchQuery) {
      const q = currentSearchQuery;
      const titleMatch = (p.title || '').toLowerCase().includes(q);
      const modelMatch = (p.model || '').toLowerCase().includes(q);
      const catMatch = (p.category || '').toLowerCase().includes(q);
      const promptMatch = (p.prompt || '').toLowerCase().includes(q);
      const tagsMatch = (p.tags || []).some(t => t.toLowerCase().includes(q));
      matchQuery = titleMatch || modelMatch || catMatch || promptMatch || tagsMatch;
    }

    return matchModel && matchQuery;
  });
}

// Render Video Card Grid
function renderGrid() {
  const filtered = getFilteredProjects();
  searchCount.textContent = filtered.length;

  if (filtered.length === 0) {
    videoGrid.innerHTML = '';
    emptyState.classList.remove('hidden');
    return;
  }

  emptyState.classList.add('hidden');
  videoGrid.innerHTML = filtered.map(p => createCardHTML(p)).join('');

  // Attach hover and click listeners to cards
  document.querySelectorAll('.video-card').forEach(card => {
    const projId = parseInt(card.dataset.id, 10);
    const proj = allProjects.find(item => item.id === projId);
    if (!proj) return;

    const videoEl = card.querySelector('.card-video-preview');

    // Hover Preview
    if (videoEl) {
      card.addEventListener('mouseenter', () => {
        videoEl.currentTime = 0;
        const playPromise = videoEl.play();
        if (playPromise !== undefined) {
          playPromise.catch(() => {});
        }
      });

      card.addEventListener('mouseleave', () => {
        videoEl.pause();
        videoEl.currentTime = 0;
      });
    }

    // Card Click -> Open Modal
    card.addEventListener('click', () => openModal(proj));
  });
}

// Card HTML Template
function createCardHTML(p) {
  const dataDir = `../data/${p.dir}`;
  const videoSrc = p.video_file ? `${dataDir}/${p.video_file}` : '';
  const thumbSrc = p.thumb_file ? `${dataDir}/${p.thumb_file}` : '';
  const duration = p.duration_sec ? `${p.duration_sec}s` : (p.aspect_ratio || '16:9');
  
  // Prompt snippet
  const promptSnippet = p.prompt ? p.prompt.slice(0, 140).trim() + '...' : 'No prompt provided.';

  return `
    <div class="video-card" data-id="${p.id}">
      <div class="card-media">
        ${thumbSrc ? `<img class="card-thumb" src="${thumbSrc}" alt="${p.title}" loading="lazy">` : `<div class="card-thumb" style="background:#1a1c24;"></div>`}
        ${videoSrc ? `<video class="card-video-preview" src="${videoSrc}" muted loop playsinline preload="none"></video>` : ''}
        
        <div class="card-floating-badges">
          <span class="badge badge-model">${p.model || 'AI Video'}</span>
          ${p.category ? `<span class="badge badge-cat">${p.category}</span>` : ''}
        </div>

        <span class="card-duration">${duration}</span>
      </div>

      <div class="card-info">
        <h3 class="card-title">${p.title}</h3>
        <p class="card-prompt-preview">${escapeHTML(promptSnippet)}</p>
        <div class="card-footer">
          <span>${p.created_at ? p.created_at.split(' ')[0] : ''}</span>
          <span>${(p.references || []).length} Ref Assets</span>
        </div>
      </div>
    </div>
  `;
}

// Open Detail Modal
function openModal(proj) {
  selectedProject = proj;
  const dataDir = `../data/${proj.dir}`;

  // Populate Meta
  modalTitle.textContent = proj.title;
  modalDate.textContent = `Registered: ${proj.created_at || 'Recently'}`;
  modalModelBadge.textContent = proj.model || 'Wan 3.0';
  modalCategoryBadge.textContent = proj.category || 'Visual Film';
  modalDurationBadge.textContent = proj.duration_sec ? `${proj.duration_sec}s` : 'Full Length';
  modalAspectBadge.textContent = proj.aspect_ratio || '16:9';

  // Video Setup
  if (proj.video_file) {
    modalVideo.src = `${dataDir}/${proj.video_file}`;
    modalVideo.classList.remove('hidden');
    modalVideoPlaceholder.classList.add('hidden');
    modalVideo.load();
    modalVideo.play().catch(() => {});
  } else {
    modalVideo.src = '';
    modalVideo.classList.add('hidden');
    modalVideoPlaceholder.classList.remove('hidden');
  }

  // Reference Images Setup
  if (proj.references && proj.references.length > 0) {
    modalRefsSection.classList.remove('hidden');
    modalRefsList.innerHTML = proj.references.map((refPath, idx) => {
      const fullRefUrl = `${dataDir}/${refPath}`;
      return `
        <div class="ref-item" onclick="window.open('${fullRefUrl}', '_blank')" title="Click to view full image">
          <img src="${fullRefUrl}" alt="Ref @Image ${idx+1}">
          <span class="ref-label">@Image ${idx+1}</span>
        </div>
      `;
    }).join('');
  } else {
    modalRefsSection.classList.add('hidden');
    modalRefsList.innerHTML = '';
  }

  // Prompt Setup
  modalPrompt.textContent = proj.prompt || '(No prompt text recorded)';

  // Reset Copy Button State
  copyPromptBtn.classList.remove('copied');
  copyPromptBtn.querySelector('.copy-text').textContent = 'Copy Prompt';

  // Show Modal
  detailModal.classList.remove('hidden');
}

// Close Modal
function closeModal() {
  detailModal.classList.add('hidden');
  modalVideo.pause();
  modalVideo.src = '';
  selectedProject = null;
}

// Copy to Clipboard
async function copyPromptToClipboard() {
  if (!selectedProject || !selectedProject.prompt) return;

  try {
    await navigator.clipboard.writeText(selectedProject.prompt);
    copyPromptBtn.classList.add('copied');
    copyPromptBtn.querySelector('.copy-text').textContent = 'Copied! ✨';
    setTimeout(() => {
      copyPromptBtn.classList.remove('copied');
      copyPromptBtn.querySelector('.copy-text').textContent = 'Copy Prompt';
    }, 2500);
  } catch (err) {
    console.error('Failed to copy text: ', err);
    // Fallback
    const textarea = document.createElement('textarea');
    textarea.value = selectedProject.prompt;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    copyPromptBtn.classList.add('copied');
    copyPromptBtn.querySelector('.copy-text').textContent = 'Copied! ✨';
  }
}

// Helper: Escape HTML
function escapeHTML(str) {
  if (!str) return '';
  return str.replace(/[&<>'"]/g, 
    tag => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      "'": '&#39;',
      '"': '&quot;'
    }[tag] || tag)
  );
}

// Start application
window.addEventListener('DOMContentLoaded', init);
