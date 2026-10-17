// Main App Logic
document.addEventListener("DOMContentLoaded", () => {
  const cardsContainer = document.getElementById("cards-grid");
  const filterBtns = document.querySelectorAll(".filter-btn");
  const searchInput = document.getElementById("search-input");
  const modalOverlay = document.getElementById("modal-overlay");
  const modalCloseBtn = document.getElementById("modal-close-btn");
  const toast = document.getElementById("toast");

  let currentCategory = "all";
  let searchQuery = "";

  // Render cards
  function renderCards() {
    cardsContainer.innerHTML = "";

    const filtered = SKILLS_DATA.filter(item => {
      const matchCategory = currentCategory === "all" || item.category === currentCategory;
      const matchSearch = searchQuery === "" || 
        item.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        item.subtitle.toLowerCase().includes(searchQuery.toLowerCase()) ||
        item.desc.toLowerCase().includes(searchQuery.toLowerCase()) ||
        item.keys.some(k => k.toLowerCase().includes(searchQuery.toLowerCase()));
      return matchCategory && matchSearch;
    });

    if (filtered.length === 0) {
      cardsContainer.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 60px 0; color: #64748b;">
          <div style="font-size: 40px; margin-bottom: 12px;">🔍</div>
          <p>일치하는 프롬프트 스킬이 없습니다.</p>
        </div>
      `;
      return;
    }

    filtered.forEach(skill => {
      const card = document.createElement("div");
      card.className = "skill-card";
      card.innerHTML = `
        <div class="card-preview">
          <div class="card-preview-bg bg-gradient-to-br ${skill.bgGradient}"></div>
          <div class="preview-overlay"></div>
          <div class="preview-badge-group">
            <span class="badge ${skill.tagColor}">${skill.tag}</span>
          </div>
          <div class="preview-specs">
            <span>${skill.aspectRatio}</span> · <span>${skill.duration}</span>
          </div>
          <div class="preview-icon-center">${skill.visualIcon}</div>
        </div>
        <div class="card-body">
          <h3 class="card-title">${skill.title}</h3>
          <div class="card-subtitle">${skill.subtitle}</div>
          <p class="card-desc">${skill.desc}</p>
          <div class="card-tags">
            ${skill.keys.map(k => `<span class="pill-tag">#${k}</span>`).join("")}
          </div>
          <div class="card-footer">
            <span class="view-detail-btn">공식 & 타임라인 보기 →</span>
            <button class="copy-quick-btn" data-id="${skill.id}">프롬프트 복사</button>
          </div>
        </div>
      `;

      // Open modal on card click
      card.addEventListener("click", (e) => {
        if (e.target.classList.contains("copy-quick-btn")) {
          e.stopPropagation();
          copyToClipboard(skill.prompt);
          showToast("📋 프롬프트가 클립보드에 복사되었습니다!");
          return;
        }
        openModal(skill);
      });

      cardsContainer.appendChild(card);
    });
  }

  // Filter click
  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      currentCategory = btn.dataset.category;
      renderCards();
    });
  });

  // Search input
  searchInput.addEventListener("input", (e) => {
    searchQuery = e.target.value.trim();
    renderCards();
  });

  // Modal open
  function openModal(skill) {
    document.getElementById("modal-badge").className = `badge ${skill.tagColor}`;
    document.getElementById("modal-badge").textContent = skill.tag;
    document.getElementById("modal-title").textContent = skill.title;
    document.getElementById("modal-subtitle").textContent = skill.subtitle;
    document.getElementById("modal-desc").textContent = skill.desc;

    // Timeline render
    const timelineContainer = document.getElementById("modal-timeline");
    timelineContainer.innerHTML = skill.timeline.map(t => `
      <div class="timeline-item">
        <div class="timeline-time">${t.time}</div>
        <div class="timeline-content">
          <strong>${t.label}</strong>
          <span>${t.detail}</span>
        </div>
      </div>
    `).join("");

    // Keys tags
    const keysContainer = document.getElementById("modal-keys");
    keysContainer.innerHTML = skill.keys.map(k => `
      <span class="pill-tag" style="background: rgba(139,92,246,0.15); color: #c084fc; border-color: rgba(139,92,246,0.3);">
        ✓ ${k}
      </span>
    `).join("");

    // Prompt text & char count
    const promptTextElem = document.getElementById("modal-prompt-text");
    promptTextElem.textContent = skill.prompt;
    document.getElementById("modal-char-count").textContent = `글자 수: ${skill.prompt.length}자 (공백 포함)`;

    // Modal copy button
    const copyFullBtn = document.getElementById("modal-copy-btn");
    copyFullBtn.onclick = () => {
      copyToClipboard(skill.prompt);
      showToast("📋 완성형 프롬프트가 복사되었습니다!");
    };

    modalOverlay.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  // Modal close
  function closeModal() {
    modalOverlay.classList.remove("active");
    document.body.style.overflow = "auto";
  }

  modalCloseBtn.addEventListener("click", closeModal);
  modalOverlay.addEventListener("click", (e) => {
    if (e.target === modalOverlay) closeModal();
  });

  // Copy helper
  function copyToClipboard(text) {
    navigator.clipboard.writeText(text);
  }

  // Toast helper
  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.add("active");
    setTimeout(() => {
      toast.classList.remove("active");
    }, 2400);
  }

  // Initial render
  renderCards();
});
