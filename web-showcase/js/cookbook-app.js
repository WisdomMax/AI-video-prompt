// AI Video Prompt Cookbook App Engine
document.addEventListener("DOMContentLoaded", () => {
  const cardsGrid = document.getElementById("cards-grid");
  const tabBtns = document.querySelectorAll(".tab-btn");
  const searchInput = document.getElementById("search-input");
  const modalOverlay = document.getElementById("modal-overlay");
  const modalClose = document.getElementById("modal-close");
  const toastMsg = document.getElementById("toast-msg");

  let activeCategory = "all";
  let searchVal = "";

  // Render cards
  function renderRecipes() {
    cardsGrid.innerHTML = "";

    const filtered = SKILLS_DATA.filter(item => {
      const matchCat = activeCategory === "all" || item.category === activeCategory;
      const matchQuery = searchVal === "" ||
        item.title.toLowerCase().includes(searchVal.toLowerCase()) ||
        item.subtitle.toLowerCase().includes(searchVal.toLowerCase()) ||
        item.howItWorks.toLowerCase().includes(searchVal.toLowerCase()) ||
        item.keys.some(k => k.toLowerCase().includes(searchVal.toLowerCase()));
      return matchCat && matchQuery;
    });

    if (filtered.length === 0) {
      cardsGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 80px 0; color: #64748b;">
          <div style="font-size: 48px; margin-bottom: 16px;">🔍</div>
          <h3 style="color: #fff; font-size: 18px; margin-bottom: 6px;">일치하는 프롬프트 레시피가 없습니다</h3>
          <p style="font-size: 14px;">다른 검색어나 카테고리를 선택해 보세요.</p>
        </div>
      `;
      return;
    }

    filtered.forEach(skill => {
      const card = document.createElement("div");
      card.className = "recipe-card";
      card.innerHTML = `
        <div class="card-banner">
          <span class="badge ${skill.tagColor}">${skill.tag}</span>
          <span class="card-specs">${skill.aspectRatio} · ${skill.duration}</span>
        </div>

        <div class="card-main">
          <h2 class="card-title">${skill.title}</h2>
          <div class="card-subtitle">${skill.subtitle}</div>
          <p class="card-desc">${skill.desc}</p>

          <!-- How It Works Educational Highlight -->
          <div class="secret-formula-box">
            <div class="secret-formula-title">
              <span>💡</span> 프롬프트 핵심 성공 비결 (Why it works)
            </div>
            <div class="secret-formula-text">${skill.howItWorks}</div>
          </div>

          <!-- Formula Snippet -->
          <div class="code-snippet-box">
            <div class="code-snippet-label">⚡ 핵심 지시어 스니펫 (Core Directives)</div>
            <pre class="code-snippet-content">${skill.formulaSnippet}</pre>
          </div>

          <!-- Actions -->
          <div class="card-actions">
            <button class="btn-detail" data-id="${skill.id}">
              <span>⏱️</span> 샷 구성 & 풀 프롬프트 보기
            </button>
            <button class="btn-copy" data-id="${skill.id}">
              <span>📋</span> 복사
            </button>
          </div>
        </div>
      `;

      // Event listeners
      card.querySelector(".btn-detail").addEventListener("click", () => openModal(skill));
      card.querySelector(".btn-copy").addEventListener("click", () => {
        copyPrompt(skill.prompt);
      });

      cardsGrid.appendChild(card);
    });
  }

  // Filter tabs
  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      tabBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      activeCategory = btn.dataset.category;
      renderRecipes();
    });
  });

  // Search
  searchInput.addEventListener("input", (e) => {
    searchVal = e.target.value.trim();
    renderRecipes();
  });

  // Open Modal
  function openModal(skill) {
    document.getElementById("modal-badge").className = `badge ${skill.tagColor}`;
    document.getElementById("modal-badge").textContent = skill.tag;
    document.getElementById("modal-title").textContent = skill.title;
    document.getElementById("modal-subtitle").textContent = skill.subtitle;
    document.getElementById("modal-why").textContent = skill.howItWorks;

    // Render timeline
    const timelineBox = document.getElementById("modal-timeline-box");
    timelineBox.innerHTML = skill.timeline.map(t => `
      <div class="timeline-row">
        <div class="timeline-time">${t.time}</div>
        <div>
          <strong style="color: #fff; margin-right: 6px;">${t.label}</strong>
          <span style="color: #94a3b8;">${t.detail}</span>
        </div>
      </div>
    `).join("");

    // Full prompt
    document.getElementById("modal-full-prompt").textContent = skill.prompt;
    document.getElementById("modal-char-count").textContent = `총 ${skill.prompt.length}자 (공백 포함)`;

    // Copy full prompt in modal
    document.getElementById("modal-copy-full-btn").onclick = () => {
      copyPrompt(skill.prompt);
    };

    modalOverlay.classList.add("active");
    document.body.style.overflow = "hidden";
  }

  // Close Modal
  function closeModal() {
    modalOverlay.classList.remove("active");
    document.body.style.overflow = "auto";
  }

  modalClose.addEventListener("click", closeModal);
  modalOverlay.addEventListener("click", (e) => {
    if (e.target === modalOverlay) closeModal();
  });

  // Copy helper
  function copyPrompt(text) {
    navigator.clipboard.writeText(text);
    toastMsg.textContent = "📋 완성형 프롬프트가 클립보드에 복사되었습니다!";
    toastMsg.classList.add("show");
    setTimeout(() => {
      toastMsg.classList.remove("show");
    }, 2400);
  }

  // Initial render
  renderRecipes();
});
