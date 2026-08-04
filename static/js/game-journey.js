/**
 * ==========================================================================
 * FOOTPRINT QUEST - GAMIFIED LEARNING JOURNEY ENGINE
 * Dynamic S-curve path drawer, interactive quizzes, AJAX progression, and confetti
 * ==========================================================================
 */

// Confetti Particle System
class ConfettiEngine {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.particles = [];
    this.isActive = false;

    window.addEventListener('resize', () => this.resize());
    this.resize();
  }

  resize() {
    this.width = this.canvas.width = window.innerWidth;
    this.height = this.canvas.height = window.innerHeight;
  }

  burst(x, y, count = 120) {
    this.particles = [];
    const colors = ['#00f0ff', '#8b5cf6', '#ff007f', '#10b981', '#f59e0b', '#3b82f6'];
    
    for (let i = 0; i < count; i++) {
      this.particles.push({
        x: x || this.width / 2,
        y: y || this.height * 0.4,
        size: Math.random() * 8 + 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        vx: (Math.random() - 0.5) * 15,
        vy: -Math.random() * 12 - 4,
        gravity: 0.28,
        drag: 0.985,
        rotation: Math.random() * Math.PI * 2,
        rotationSpeed: (Math.random() - 0.5) * 0.2,
        alpha: 1,
        fadeSpeed: Math.random() * 0.01 + 0.005
      });
    }

    if (!this.isActive) {
      this.isActive = true;
      this.animate();
    }
  }

  animate() {
    if (this.particles.length === 0) {
      this.isActive = false;
      this.ctx.clearRect(0, 0, this.width, this.height);
      return;
    }

    this.ctx.clearRect(0, 0, this.width, this.height);

    for (let i = this.particles.length - 1; i >= 0; i--) {
      const p = this.particles[i];
      p.vx *= p.drag;
      p.vy += p.gravity;
      p.vy *= p.drag;
      p.x += p.vx;
      p.y += p.vy;
      p.rotation += p.rotationSpeed;
      p.alpha -= p.fadeSpeed;

      if (p.alpha <= 0 || p.y > this.height) {
        this.particles.splice(i, 1);
        continue;
      }

      this.ctx.save();
      this.ctx.translate(p.x, p.y);
      this.ctx.rotate(p.rotation);
      this.ctx.fillStyle = p.color;
      this.ctx.globalAlpha = p.alpha;
      
      // Draw rectangular confetti piece
      this.ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 1.5);
      this.ctx.restore();
    }

    requestAnimationFrame(() => this.animate());
  }
}

// Game Map & Level Modal Interactions
class GameJourneyMap {
  constructor() {
    this.mapWrapper = document.querySelector('.map-wrapper');
    this.nodesMap = document.getElementById('levels-map');
    this.connectionLine = document.getElementById('map-connection-line');
    this.progressLine = document.getElementById('map-progress-line');
    this.modal = document.getElementById('level-modal');
    this.modalClose = document.getElementById('level-modal-close');
    
    this.btnComplete = document.getElementById('btn-complete-level');
    this.modalTitle = document.getElementById('modal-level-title');
    this.modalTag = document.getElementById('modal-level-tag');
    this.modalIcon = document.getElementById('modal-level-icon-badge');
    this.modalLesson = document.getElementById('modal-lesson-content');
    this.modalQuestion = document.getElementById('modal-challenge-question');
    this.modalChoices = document.getElementById('modal-challenge-choices');
    this.feedbackArea = document.getElementById('challenge-feedback');
    
    this.confetti = new ConfettiEngine('confetti-canvas');
    this.activeLevelData = null;
    this.selectedCorrectChoice = false;

    if (this.nodesMap) {
      this.initEvents();
      // Draw lines after layout has fully calculated
      setTimeout(() => this.drawConnectionPath(), 300);
    }
  }

  initEvents() {
    // Resize handler for redrawing path lines
    window.addEventListener('resize', () => this.drawConnectionPath());

    // Bind level node clicks
    const nodeWrappers = document.querySelectorAll('.level-node-wrapper');
    nodeWrappers.forEach(wrapper => {
      const nodeBtn = wrapper.querySelector('.level-node');
      nodeBtn.addEventListener('click', (e) => {
        const level = parseInt(wrapper.getAttribute('data-level'));
        const status = wrapper.getAttribute('data-status');
        
        if (status === 'locked') {
          this.triggerNodeLockShake(wrapper);
        } else {
          this.openLevelModal(wrapper);
        }
      });
    });

    // Bind modal close
    if (this.modalClose) {
      this.modalClose.addEventListener('click', () => this.closeLevelModal());
    }

    // Complete Level Click
    if (this.btnComplete) {
      this.btnComplete.addEventListener('click', () => this.completeActiveLevel());
    }
  }

  // Draw smooth S-curve connecting path
  drawConnectionPath() {
    if (!this.mapWrapper || !this.connectionLine || !this.progressLine) return;
    
    const wrappers = Array.from(document.querySelectorAll('.level-node-wrapper'));
    if (wrappers.length === 0) return;

    // Get positions relative to map wrapper
    const wrapperRect = this.mapWrapper.getBoundingClientRect();
    const points = [];
    let activeIndex = -1;

    wrappers.forEach((wrapper, index) => {
      const btn = wrapper.querySelector('.level-node');
      const btnRect = btn.getBoundingClientRect();
      
      const x = btnRect.left - wrapperRect.left + btnRect.width / 2;
      const y = btnRect.top - wrapperRect.top + btnRect.height / 2;
      points.push({ x, y, status: wrapper.getAttribute('data-status') });
      
      if (wrapper.getAttribute('data-status') === 'unlocked') {
        activeIndex = index;
      }
    });

    if (points.length === 0) return;

    // Generate smooth Cubic Bezier path string
    let d = `M ${points[0].x} ${points[0].y}`;
    for (let i = 0; i < points.length - 1; i++) {
      const p1 = points[i];
      const p2 = points[i+1];
      const cp1x = p1.x;
      const cp1y = p1.y + (p2.y - p1.y) * 0.55;
      const cp2x = p2.x;
      const cp2y = p1.y + (p2.y - p1.y) * 0.55;
      d += ` C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${p2.x} ${p2.y}`;
    }

    this.connectionLine.setAttribute('d', d);

    // Generate progress path string (up to active unlocked node)
    let progressD = "";
    const progressLimit = activeIndex >= 0 ? activeIndex : points.length - 1;
    
    if (progressLimit > 0) {
      progressD = `M ${points[0].x} ${points[0].y}`;
      for (let i = 0; i < progressLimit; i++) {
        const p1 = points[i];
        const p2 = points[i+1];
        const cp1x = p1.x;
        const cp1y = p1.y + (p2.y - p1.y) * 0.55;
        const cp2x = p2.x;
        const cp2y = p1.y + (p2.y - p1.y) * 0.55;
        progressD += ` C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${p2.x} ${p2.y}`;
      }
    }
    
    this.progressLine.setAttribute('d', progressD);
  }

  // Locked node click feedack
  triggerNodeLockShake(wrapper) {
    const node = wrapper.querySelector('.level-node');
    node.style.animation = 'none';
    // Trigger browser reflow
    void node.offsetWidth;
    node.style.animation = 'shakeBtn 0.4s ease';

    // Show locked toast message
    const tooltip = wrapper.querySelector('.level-tooltip');
    if (tooltip) {
      tooltip.style.opacity = '1';
      tooltip.style.transform = 'translateY(0) scale(1)';
      setTimeout(() => {
        tooltip.style.opacity = '';
        tooltip.style.transform = '';
      }, 1500);
    }
  }

  // Level Details modal population
  openLevelModal(wrapper) {
    const level = parseInt(wrapper.getAttribute('data-level'));
    const status = wrapper.getAttribute('data-status');
    const title = wrapper.getAttribute('data-title');
    const description = wrapper.getAttribute('data-description');
    const icon = wrapper.getAttribute('data-icon');
    const lesson = wrapper.getAttribute('data-lesson');
    const question = wrapper.getAttribute('data-question');
    const choices = JSON.parse(wrapper.getAttribute('data-choices'));
    const correctIdx = parseInt(wrapper.getAttribute('data-correct'));

    this.activeLevelData = { level, status, title, icon, correctIdx };
    this.selectedCorrectChoice = false;

    // Set Modal texts
    this.modalTag.textContent = `LEVEL ${level}`;
    this.modalTitle.textContent = title;
    this.modalIcon.innerHTML = `<i class="fa-solid ${icon}"></i>`;
    this.modalLesson.innerHTML = lesson;
    
    // Setup Challenge Section
    this.feedbackArea.style.display = 'none';
    this.btnComplete.disabled = true;

    // For level 1 (Create Account) - no quiz questions
    if (level === 1) {
      this.modalQuestion.innerHTML = `<div class="status-badge completed" style="font-size: 1rem;"><i class="fa-solid fa-check"></i> Account Authenticated</div><p style="margin-top:1rem;">Your account is ready! Launch details verified.</p>`;
      this.modalChoices.innerHTML = '';
      this.btnComplete.disabled = false;
      this.selectedCorrectChoice = true;
    } else {
      this.modalQuestion.innerHTML = question;
      this.modalChoices.innerHTML = '';
      
      choices.forEach((choice, index) => {
        const btn = document.createElement('button');
        btn.className = 'choice-btn';
        btn.innerHTML = choice;
        
        // Handle choice click
        btn.addEventListener('click', () => {
          if (status === 'completed') return; // Read-only if already completed
          
          // Reset classes of all buttons
          const btns = this.modalChoices.querySelectorAll('.choice-btn');
          btns.forEach(b => b.className = 'choice-btn');
          
          if (index === correctIdx) {
            btn.classList.add('selected-correct');
            this.showFeedback(true, "Correct! Sovereignty challenge passed.");
            this.btnComplete.disabled = false;
            this.selectedCorrectChoice = true;
          } else {
            btn.classList.add('selected-incorrect');
            this.showFeedback(false, "Incorrect vector analysis. Please try again.");
            this.btnComplete.disabled = true;
            this.selectedCorrectChoice = false;
          }
        });

        // Pre-select if already completed
        if (status === 'completed') {
          btn.disabled = true;
          if (index === correctIdx) {
            btn.classList.add('selected-correct');
          }
        }

        this.modalChoices.appendChild(btn);
      });

      if (status === 'completed') {
        this.showFeedback(true, "Level Completed! Verified 100 XP.");
        this.btnComplete.innerHTML = `<i class="fa-solid fa-circle-check"></i> Level Already Completed`;
        this.btnComplete.disabled = true;
      } else {
        this.btnComplete.innerHTML = `<i class="fa-solid fa-bolt"></i> Complete Level & Claim 100 XP`;
      }
    }

    // Open Modal
    this.modal.classList.add('active');
  }

  showFeedback(isCorrect, text) {
    this.feedbackArea.style.display = 'block';
    this.feedbackArea.className = isCorrect ? 'challenge-feedback correct-feedback' : 'challenge-feedback incorrect-feedback';
    this.feedbackArea.querySelector('.feedback-text').textContent = text;
  }

  closeLevelModal() {
    this.modal.classList.remove('active');
    this.activeLevelData = null;
  }

  // Complete Active Level AJAX call
  completeActiveLevel() {
    if (!this.activeLevelData || !this.selectedCorrectChoice) return;
    
    const level = this.activeLevelData.level;
    const csrfToken = document.getElementById('csrf-token-holder').value;

    fetch('/journey/complete-level/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({ level: level })
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        this.closeLevelModal();
        
        // Trigger full-screen celebration burst
        this.confetti.burst();
        
        // Update User stats in DOM
        const xpText = document.getElementById('user-xp-display');
        if (xpText) {
          this.animateXPCount(parseInt(xpText.textContent), data.xp, xpText);
        }

        // Wait brief delay then reload page to update state smoothly, or update nodes in place
        setTimeout(() => {
          window.location.reload();
        }, 1200);
      } else {
        alert(data.message || 'Error updating quest progress.');
      }
    })
    .catch(err => {
      console.error("Quest submission error:", err);
      alert("Failed to submit challenge.");
    });
  }

  // Animates the XP digits increasing
  animateXPCount(start, end, element) {
    let current = start;
    const step = Math.ceil((end - start) / 15);
    const timer = setInterval(() => {
      current += step;
      if (current >= end) {
        clearInterval(timer);
        element.textContent = end;
      } else {
        element.textContent = current;
      }
    }, 40);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new GameJourneyMap();
});
