/**
 * ==========================================================================
 * FOOTPRINT QUEST - GAMIFIED LEARNING JOURNEY ENGINE
 * Dynamic S-curve path drawer, interactive quizzes, 8 mini-games, and confetti
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
    
    // Scenario elements
    this.btnNext = document.getElementById('btn-next-scenario');
    this.modalTitle = document.getElementById('modal-level-title');
    this.modalTag = document.getElementById('modal-level-tag');
    this.modalIcon = document.getElementById('modal-level-icon-badge');
    this.modalLessonColumn = document.getElementById('modal-lesson-column');
    this.modalChallengeColumn = document.getElementById('modal-challenge-column');
    
    this.modalLesson = document.getElementById('modal-lesson-content');
    this.modalQuestion = document.getElementById('modal-challenge-question');
    this.modalChoices = document.getElementById('modal-challenge-choices');
    this.feedbackArea = document.getElementById('challenge-feedback');
    this.currentCardNum = document.getElementById('current-card-num');
    this.totalCardsNum = document.getElementById('total-cards-num');
    
    // Mini-game container
    this.minigameContainer = document.getElementById('minigame-container');
    
    // Mascot elements
    this.mascotBubble = document.getElementById('mascot-modal-bubble');
    this.mascotMouth = document.getElementById('mascot-modal-mouth');
    this.mascotEyelids = document.querySelectorAll('.mascot-modal-eyelid');

    this.confetti = new ConfettiEngine('confetti-canvas');
    this.activeLevel = 0;
    this.activeLevelType = "";
    
    // Scenario game tracking
    this.scenarios = [];
    this.currentScenarioIndex = 0;
    this.correctAnswers = 0;
    this.wrongAnswers = 0;
    
    // Temporary accumulated score diffs for session
    this.privacyDiff = 0;
    this.securityDiff = 0;
    this.reputationDiff = 0;
    this.trustDiff = 0;

    if (this.nodesMap) {
      this.initEvents();
      this.initBlinking();
      setTimeout(() => this.drawConnectionPath(), 300);
    }
  }

  initEvents() {
    window.addEventListener('resize', () => this.drawConnectionPath());

    const nodeWrappers = document.querySelectorAll('.level-node-wrapper');
    nodeWrappers.forEach(wrapper => {
      const nodeBtn = wrapper.querySelector('.level-node');
      nodeBtn.addEventListener('click', () => {
        const level = parseInt(wrapper.getAttribute('data-level'));
        const status = wrapper.getAttribute('data-status');
        
        if (status === 'locked') {
          this.triggerNodeLockShake(wrapper);
        } else {
          this.fetchLevelData(level);
        }
      });
    });

    if (this.modalClose) {
      this.modalClose.addEventListener('click', () => this.closeLevelModal());
    }

    if (this.btnNext) {
      this.btnNext.addEventListener('click', () => this.handleNextOrSubmit());
    }
  }

  initBlinking() {
    const blink = () => {
      if (this.mascotEyelids) {
        this.mascotEyelids.forEach(el => el.style.display = 'block');
        setTimeout(() => {
          this.mascotEyelids.forEach(el => el.style.display = 'none');
        }, 140);
      }
      setTimeout(blink, Math.random() * 4000 + 2000);
    };
    setTimeout(blink, 2000);
  }

  updateMascotFace(expression, bubbleText) {
    if (this.mascotBubble) {
      this.mascotBubble.textContent = bubbleText;
    }
    if (this.mascotMouth) {
      if (expression === 'happy') {
        this.mascotMouth.setAttribute('d', 'M 40 62 Q 50 74 60 62'); // Smile
      } else if (expression === 'sad') {
        this.mascotMouth.setAttribute('d', 'M 40 68 Q 50 56 60 68'); // Frown
      } else {
        this.mascotMouth.setAttribute('d', 'M 42 64 Q 50 70 58 64'); // Neutral
      }
    }
  }

  drawConnectionPath() {
    if (!this.mapWrapper || !this.connectionLine || !this.progressLine) return;
    
    const wrappers = Array.from(document.querySelectorAll('.level-node-wrapper'));
    if (wrappers.length === 0) return;

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

  triggerNodeLockShake(wrapper) {
    const node = wrapper.querySelector('.level-node');
    node.style.animation = 'none';
    void node.offsetWidth;
    node.style.animation = 'shakeBtn 0.4s ease';

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

  closeLevelModal() {
    this.modal.classList.remove('active');
  }

  fetchLevelData(levelId) {
    fetch(`/journey/level-data/${levelId}/`)
      .then(res => {
        // Django redirects protected endpoints to the login page.  Follow that
        // redirect in the browser instead of attempting to parse HTML as JSON.
        if (res.redirected) {
          window.location.assign(res.url);
          return null;
        }
        if (!res.ok) {
          throw new Error(`Unable to load level (${res.status}).`);
        }
        return res.json();
      })
      .then(data => {
        if (!data) return;
        if (data.status === 'error') {
          alert(data.message);
          return;
        }
        this.openLevelModal(data);
      })
      .catch(err => {
        console.error("Error loading level details:", err);
      });
  }

  openLevelModal(data) {
    this.activeLevel = data.level;
    this.activeLevelType = data.type;
    
    // Header tags
    this.modalTag.textContent = `LEVEL ${data.level}`;
    this.modalTitle.textContent = data.title;
    this.modalIcon.innerHTML = `<i class="fa-solid ${data.icon}"></i>`;
    
    this.updateMascotFace('neutral', `Welcome to Level ${data.level}! Let's do this.`);

    // Check level type and configure modal panels
    if (data.type === "scenario" || data.type === "game_escape") {
      this.modalLessonColumn.style.display = "flex";
      this.modalChallengeColumn.style.display = "flex";
      this.minigameContainer.style.display = "none";
      
      this.scenarios = data.scenarios;
      this.currentScenarioIndex = 0;
      this.correctAnswers = 0;
      this.wrongAnswers = 0;
      
      this.privacyDiff = 0;
      this.securityDiff = 0;
      this.reputationDiff = 0;
      this.trustDiff = 0;
      
      this.totalCardsNum.textContent = this.scenarios.length;
      this.loadScenarioCard();
    } else {
      // It is a mini-game level!
      this.modalLessonColumn.style.display = "none";
      this.modalChallengeColumn.style.display = "none";
      this.minigameContainer.style.display = "block";
      
      this.initializeMiniGame(data);
    }

    this.modal.classList.add('active');
  }

  // Load a single scenario card
  loadScenarioCard() {
    if (this.currentScenarioIndex >= this.scenarios.length) return;
    
    const sc = this.scenarios[this.currentScenarioIndex];
    this.currentCardNum.textContent = this.currentScenarioIndex + 1;
    
    // Build story briefing description
    this.modalLesson.innerHTML = `<p>${sc.story}</p>`;
    this.modalQuestion.textContent = "What is the best security decision to make?";
    
    this.modalChoices.innerHTML = "";
    this.feedbackArea.style.display = "none";
    this.btnNext.disabled = true;
    
    if (this.currentScenarioIndex === this.scenarios.length - 1) {
      this.btnNext.innerHTML = `Complete Quest <i class="fa-solid fa-circle-check"></i>`;
    } else {
      this.btnNext.innerHTML = `Next Decision <i class="fa-solid fa-arrow-right"></i>`;
    }

    sc.choices.forEach((choice, index) => {
      const btn = document.createElement('button');
      btn.className = "choice-btn";
      btn.innerHTML = choice;
      
      btn.addEventListener('click', () => {
        // Disable choices
        const btns = this.modalChoices.querySelectorAll('.choice-btn');
        btns.forEach(b => b.disabled = true);
        
        if (index === sc.correct_idx) {
          btn.classList.add('selected-correct');
          this.correctAnswers++;
          this.showFeedback(true, sc.feedback || "Correct! That is the safest action.");
          this.updateMascotFace('happy', "Spot on! That helps keep your digital score high.");
          
          // Accumulate positive differentials
          this.privacyDiff += 5;
          this.securityDiff += 5;
          this.reputationDiff += 5;
        } else {
          btn.classList.add('selected-incorrect');
          this.wrongAnswers++;
          this.showFeedback(false, sc.feedback || "Incorrect action. This leaks metadata details.");
          this.updateMascotFace('sad', "Oh no! That decision increases your footprint footprint footprint.");
          
          // Deduct score differentials
          this.privacyDiff -= 5;
          this.securityDiff -= 5;
          this.reputationDiff -= 5;
        }
        this.btnNext.disabled = false;
      });
      
      this.modalChoices.appendChild(btn);
    });
  }

  showFeedback(isCorrect, text) {
    this.feedbackArea.style.display = "block";
    this.feedbackArea.className = isCorrect ? "challenge-feedback correct-feedback" : "challenge-feedback incorrect-feedback";
    this.feedbackArea.querySelector('.feedback-text').textContent = text;
  }

  handleNextOrSubmit() {
    this.currentScenarioIndex++;
    if (this.currentScenarioIndex < this.scenarios.length) {
      this.loadScenarioCard();
    } else {
      // Completed all scenario questions, post results to DB
      this.submitGameCompletion({
        level: this.activeLevel,
        xp: 100,
        coins: 20 + (this.correctAnswers * 5),
        stars: this.wrongAnswers === 0 ? 3 : (this.wrongAnswers <= 2 ? 2 : 1),
        correct_count: this.correctAnswers,
        wrong_count: this.wrongAnswers,
        privacy_diff: this.privacyDiff,
        security_diff: this.securityDiff,
        reputation_diff: this.reputationDiff,
        trust_diff: this.trustDiff
      });
    }
  }

  // Submit complete details to backend
  submitGameCompletion(payload) {
    const csrfToken = document.getElementById('csrf-token-holder').value;
    
    fetch('/journey/submit/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify(payload)
    })
    .then(res => {
      if (res.redirected) {
        window.location.assign(res.url);
        return null;
      }
      if (!res.ok) {
        throw new Error(`Unable to save progress (${res.status}).`);
      }
      return res.json();
    })
    .then(data => {
      if (!data) return;
      if (data.status === 'success') {
        this.closeLevelModal();
        this.confetti.burst();
        
        // Show unlocked badge alerts if present
        if (data.unlocked_badges && data.unlocked_badges.length > 0) {
          setTimeout(() => {
            alert(`🎉 ACHIEVEMENT UNLOCKED: ${data.unlocked_badges.join(', ')}! Check your rewards.`);
          }, 400);
        }

        setTimeout(() => {
          window.location.reload();
        }, 1500);
      } else {
        alert(data.message || 'Submission error.');
      }
    })
    .catch(err => {
      console.error("Submission failed:", err);
    });
  }

  // ==========================================================================
  // MINI-GAME CONSTRUCTORS AND ENGINE CODE
  // ==========================================================================
  initializeMiniGame(data) {
    this.minigameContainer.innerHTML = "";
    
    // Heading
    const header = document.createElement('div');
    header.style.marginBottom = "1.5rem";
    header.innerHTML = `<h3><i class="fa-solid fa-puzzle-piece"></i> ${data.title} Challenge</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem;">${data.description}</p>`;
    this.minigameContainer.appendChild(header);

    const gameDiv = document.createElement('div');
    this.minigameContainer.appendChild(gameDiv);

    // Call game setup based on level ID
    if (this.activeLevel === 6) this.setupPasswordGame(gameDiv);
    else if (this.activeLevel === 7) this.setupWifiGame(gameDiv);
    else if (this.activeLevel === 9) this.setupScamGame(gameDiv);
    else if (this.activeLevel === 10) this.setupPhishGame(gameDiv);
    else if (this.activeLevel === 11) this.setupSettingsGame(gameDiv);
    else if (this.activeLevel === 12) this.setupCookieGame(gameDiv);
    else if (this.activeLevel === 13) this.setupPermissionGame(gameDiv);
    else if (this.activeLevel === 19) this.setupMatchGame(gameDiv);
  }

  // 1. Password Builder Game
  setupPasswordGame(container) {
    this.updateMascotFace('neutral', "Create a passphrase with a strength above 80% to proceed!");
    
    const wrapper = document.createElement('div');
    wrapper.innerHTML = `
      <div class="passgame-input-container">
        <input type="text" class="passgame-input" id="pass-input" placeholder="Click tokens below to build password..." readonly>
        <button class="btn btn-secondary" id="pass-clear"><i class="fa-solid fa-eraser"></i> Clear</button>
      </div>
      <div class="passgame-strength-meter">
        <div class="passgame-strength-fill" id="pass-fill"></div>
      </div>
      <div class="passgame-strength-text" id="pass-text">Strength: 0% (Weak)</div>
      
      <div class="passgame-tokens" id="pass-tokens"></div>
      
      <button class="btn btn-glow" id="pass-submit" style="width:100%; padding:0.85rem;" disabled>Submit Passphrase</button>
    `;
    container.appendChild(wrapper);

    const tokens = ['green', 'cow', 'jupiter', 'coffee', '4', 'ocean', 'mars', 'danced', 'blue', 'whale', 'jupiter', '8', '!', '@', '2026', 'secure'];
    const passInput = document.getElementById('pass-input');
    const passClear = document.getElementById('pass-clear');
    const passFill = document.getElementById('pass-fill');
    const passText = document.getElementById('pass-text');
    const passSubmit = document.getElementById('pass-submit');
    const tokenContainer = document.getElementById('pass-tokens');

    let currentPass = [];

    const updateStrength = () => {
      const pass = currentPass.join('-');
      passInput.value = pass;
      
      // Compute strength
      let score = 0;
      if (currentPass.length >= 3) score = 40;
      if (currentPass.length >= 4) score = 70;
      if (currentPass.length >= 5) score = 90;
      
      // Bonus if it contains numbers/symbols
      const hasNumber = currentPass.some(t => !isNaN(t));
      const hasSymbol = currentPass.some(t => ['!', '@'].includes(t));
      if (hasNumber && score > 0) score += 10;
      if (hasSymbol && score > 0) score += 10;
      
      score = Math.min(100, score);
      
      // Render colors
      passFill.style.width = `${score}%`;
      if (score >= 80) {
        passFill.style.background = "var(--accent-emerald)";
        passText.innerHTML = `Strength: ${score}% (Strong & Secure!)`;
        passSubmit.disabled = false;
        this.updateMascotFace('happy', "Perfect! That is a robust, unhackable passphrase!");
      } else if (score >= 50) {
        passFill.style.background = "#f59e0b";
        passText.innerHTML = `Strength: ${score}% (Medium - Add more words)`;
        passSubmit.disabled = true;
      } else {
        passFill.style.background = "#ef4444";
        passText.innerHTML = `Strength: ${score}% (Weak - Append words)`;
        passSubmit.disabled = true;
      }
    };

    tokens.forEach(tok => {
      const btn = document.createElement('button');
      btn.className = 'passgame-token-btn';
      btn.textContent = tok;
      btn.addEventListener('click', () => {
        currentPass.push(tok);
        updateStrength();
      });
      tokenContainer.appendChild(btn);
    });

    passClear.addEventListener('click', () => {
      currentPass = [];
      updateStrength();
    });

    passSubmit.addEventListener('click', () => {
      this.submitGameCompletion({
        level: 6, xp: 100, coins: 25, stars: 3, correct_count: 1, wrong_count: 0,
        privacy_diff: 5, security_diff: 15, reputation_diff: 5, trust_diff: 5
      });
    });
  }

  // 2. Public Wi-Fi sorting game
  setupWifiGame(container) {
    this.updateMascotFace('neutral', "Sort these Public Wi-Fi hotspots! Safe or Unsafe?");
    
    const wrapper = document.createElement('div');
    wrapper.className = "wifigame-layout";
    wrapper.innerHTML = `
      <div class="wifigame-card-box">
        <div class="wifigame-card-inner" id="wifi-card">
          <div class="wifigame-card-title" id="wifi-title">Network Name</div>
          <div class="wifigame-card-desc" id="wifi-desc">Security Details</div>
        </div>
      </div>
      <div class="wifigame-btn-bar">
        <button class="wifigame-btn btn-unsafe" id="wifi-unsafe"><i class="fa-solid fa-triangle-exclamation"></i> UNSAFE</button>
        <button class="wifigame-btn btn-safe" id="wifi-safe"><i class="fa-solid fa-shield"></i> SAFE</button>
      </div>
      <p style="margin-top: 1.5rem; color:var(--text-muted); font-size:0.85rem;" id="wifi-progress">Hotspot: 1/4</p>
    `;
    container.appendChild(wrapper);

    const hotspots = [
      { name: "Starbucks_Guest_Open", desc: "No password, open portal landing page.", safe: false },
      { name: "Home_WiFi_WPA3", desc: "Encrypted, requires password key.", safe: true },
      { name: "Airport_Free_Network", desc: "Unsecured public hotspot.", safe: false },
      { name: "Library_Public_VPN_Encrypted", desc: "Requires portal authentication, encrypted tunnel.", safe: true }
    ];

    let currentIdx = 0;
    let mistakes = 0;

    const loadHotspot = () => {
      if (currentIdx >= hotspots.length) {
        // Game completed!
        const correct = hotspots.length - mistakes;
        this.submitGameCompletion({
          level: 7, xp: 100, coins: 20, stars: mistakes === 0 ? 3 : 1,
          correct_count: correct, wrong_count: mistakes,
          privacy_diff: 5, security_diff: 10, reputation_diff: 2, trust_diff: 5
        });
        return;
      }
      
      const hs = hotspots[currentIdx];
      document.getElementById('wifi-title').textContent = hs.name;
      document.getElementById('wifi-desc').textContent = hs.desc;
      document.getElementById('wifi-progress').textContent = `Hotspot: ${currentIdx + 1}/${hotspots.length}`;
      
      // Reset card visual state
      const card = document.getElementById('wifi-card');
      card.style.borderColor = 'var(--primary-cyan)';
    };

    const handleAnswer = (choiceSafe) => {
      const hs = hotspots[currentIdx];
      const card = document.getElementById('wifi-card');
      
      if (hs.safe === choiceSafe) {
        card.style.borderColor = 'var(--accent-emerald)';
        this.updateMascotFace('happy', "Spot on! That hotspot classification is correct.");
      } else {
        card.style.borderColor = '#ef4444';
        mistakes++;
        this.updateMascotFace('sad', "Warning! Classifying that hotspot incorrectly exposes your data traffic.");
      }
      
      currentIdx++;
      setTimeout(loadHotspot, 800);
    };

    document.getElementById('wifi-unsafe').addEventListener('click', () => handleAnswer(false));
    document.getElementById('wifi-safe').addEventListener('click', () => handleAnswer(true));

    loadHotspot();
  }

  // 3. Fake Websites Domain Spotter
  setupScamGame(container) {
    this.updateMascotFace('neutral', "Click the suspicious part of the URL address below!");
    
    const wrapper = document.createElement('div');
    wrapper.innerHTML = `
      <div class="scamgame-url-card">
        <div class="scamgame-url-text" id="scam-url"></div>
      </div>
      <p style="text-align:center; font-size:0.9rem; color:var(--text-muted);" id="scam-hint">Target: Find the fake domain section.</p>
      <button class="btn btn-glow" id="scam-submit" style="width:100%; margin-top:1.5rem;" disabled>Next URL</button>
    `;
    container.appendChild(wrapper);

    const urls = [
      {
        parts: ["https://", "www.netflix", "-login-security", ".com", "/signin"],
        fakeIdx: 2,
        desc: "The domain is 'netflix-login-security.com', not netflix.com. This is a scam copy."
      },
      {
        parts: ["https://", "accounts.google", ".security-recovery", ".net", "/verify"],
        fakeIdx: 2,
        desc: "The suffix '.net' and domain '.security-recovery' belong to hackers, not Google.com."
      }
    ];

    let currentIdx = 0;
    let selectedIdx = -1;

    const loadUrl = () => {
      selectedIdx = -1;
      document.getElementById('scam-submit').disabled = true;
      
      const sc = urls[currentIdx];
      const urlDiv = document.getElementById('scam-url');
      urlDiv.innerHTML = "";
      
      sc.parts.forEach((p, idx) => {
        const span = document.createElement('span');
        span.textContent = p;
        span.addEventListener('click', () => {
          // Reset highlights
          const spans = urlDiv.querySelectorAll('span');
          spans.forEach(s => s.className = "");
          
          span.className = "flagged";
          selectedIdx = idx;
          document.getElementById('scam-submit').disabled = false;
        });
        urlDiv.appendChild(span);
      });
    };

    document.getElementById('scam-submit').addEventListener('click', () => {
      const sc = urls[currentIdx];
      if (selectedIdx === sc.fakeIdx) {
        this.updateMascotFace('happy', "Awesome job! You spotted the replica subdomain trick.");
        alert(`Correct! ${sc.desc}`);
      } else {
        this.updateMascotFace('sad', "Wrong part clicked. Spot the added domain parameters.");
        alert(`Incorrect. ${sc.desc}`);
      }
      
      currentIdx++;
      if (currentIdx < urls.length) {
        loadUrl();
      } else {
        this.submitGameCompletion({
          level: 9, xp: 100, coins: 20, stars: 3, correct_count: 2, wrong_count: 0,
          privacy_diff: 5, security_diff: 15, reputation_diff: 2, trust_diff: 10
        });
      }
    });

    loadUrl();
  }

  // 4. Phishing Email Detective
  setupPhishGame(container) {
    this.updateMascotFace('neutral', "Click the 3 suspicious clue regions in this email!");
    
    const wrapper = document.createElement('div');
    wrapper.innerHTML = `
      <div class="detective-email-box">
        <div class="detective-header">
          <div class="detective-header-row"><strong>From:</strong> <span class="detective-clue-span" id="clue-from">support@paypaI-billing.com</span></div>
          <div class="detective-header-row"><strong>Subject:</strong> <span class="detective-clue-span" id="clue-sub">URGENT: Verify your billing info within 24 hours!</span></div>
        </div>
        <div class="detective-body">
          Dear customer, <br><br>
          We detected access requests from another country. Please click <span class="detective-clue-span" id="clue-link">http://paypal-verification-portal.com</span> to restore your account.
        </div>
      </div>
      <p style="text-align:center; font-size:0.9rem; color:var(--text-muted);" id="phish-progress">Clues found: 0/3</p>
      <button class="btn btn-glow" id="phish-submit" style="width:100%; margin-top:1.5rem;" disabled>Complete Investigation</button>
    `;
    container.appendChild(wrapper);

    const clues = ["clue-from", "clue-sub", "clue-link"];
    let found = [];

    const updateCluesProgress = () => {
      document.getElementById('phish-progress').textContent = `Clues found: ${found.length}/3`;
      if (found.length === 3) {
        document.getElementById('phish-submit').disabled = false;
        this.updateMascotFace('happy', "Amazing! You found all red flags: fake email spelling, urgent threats, and unsecured links.");
      }
    };

    clues.forEach(cid => {
      const el = document.getElementById(cid);
      el.addEventListener('click', () => {
        if (!found.includes(cid)) {
          el.className = "detective-clue-span found";
          found.push(cid);
          updateCluesProgress();
        }
      });
    });

    document.getElementById('phish-submit').addEventListener('click', () => {
      this.submitGameCompletion({
        level: 10, xp: 100, coins: 25, stars: 3, correct_count: 3, wrong_count: 0,
        privacy_diff: 5, security_diff: 15, reputation_diff: 5, trust_diff: 10
      });
    });
  }

  // 5. Settings Puzzle Toggles
  setupSettingsGame(container) {
    this.updateMascotFace('neutral', "Configure your profile toggles! Only enable secure, private options.");
    
    const wrapper = document.createElement('div');
    wrapper.className = "settingsgame-list";
    wrapper.innerHTML = `
      <div class="settingsgame-item">
        <div class="settingsgame-label">
          <h4>Send Analytics Logs</h4>
          <p>Transmits tracking and search histories to marketing partners.</p>
        </div>
        <input type="checkbox" id="set-analytics" class="switch-input">
        <label for="set-analytics" class="switch-label"></label>
      </div>

      <div class="settingsgame-item">
        <div class="settingsgame-label">
          <h4>Block Tracker Cookies</h4>
          <p>Restricts third-party cookies from monitoring across websites.</p>
        </div>
        <input type="checkbox" id="set-cookies" class="switch-input">
        <label for="set-cookies" class="switch-label"></label>
      </div>

      <div class="settingsgame-item">
        <div class="settingsgame-label">
          <h4>Share GPS Coordinates</h4>
          <p>Exposes real-time location to advertiser search filters.</p>
        </div>
        <input type="checkbox" id="set-gps" class="switch-input">
        <label for="set-gps" class="switch-label"></label>
      </div>

      <div class="settingsgame-item">
        <div class="settingsgame-label">
          <h4>Enforce HTTPS Only</h4>
          <p>Encrypts all connection traffic to prevent data leaks.</p>
        </div>
        <input type="checkbox" id="set-https" class="switch-input">
        <label for="set-https" class="switch-label"></label>
      </div>
      
      <button class="btn btn-glow" id="set-submit" style="width:100%; margin-top:1rem;">Verify Settings</button>
    `;
    container.appendChild(wrapper);

    document.getElementById('set-submit').addEventListener('click', () => {
      const analytics = document.getElementById('set-analytics').checked;
      const cookies = document.getElementById('set-cookies').checked;
      const gps = document.getElementById('set-gps').checked;
      const https = document.getElementById('set-https').checked;

      // Correct config: analytics OFF (false), cookies ON (true), gps OFF (false), https ON (true)
      if (!analytics && cookies && !gps && https) {
        this.updateMascotFace('happy', "Perfect! Your profile configuration is highly secure.");
        this.submitGameCompletion({
          level: 11, xp: 100, coins: 20, stars: 3, correct_count: 4, wrong_count: 0,
          privacy_diff: 15, security_diff: 10, reputation_diff: 5, trust_diff: 5
        });
      } else {
        this.updateMascotFace('sad', "Profile configuration is unsafe! Telemetry and tracking must be restricted.");
        alert("Incorrect settings. Review toggles and check descriptions again.");
      }
    });
  }

  // 6. Cookie Monster sorting game
  setupCookieGame(container) {
    this.updateMascotFace('neutral', "Sort cookies! Accept functional, reject analytics/tracking.");
    
    const wrapper = document.createElement('div');
    wrapper.className = "cookiegame-layout";
    wrapper.innerHTML = `
      <div class="cookiegame-monster">
        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="45" fill="#3b82f6" stroke="#00f0ff" stroke-width="3" />
          <circle cx="35" cy="40" r="10" fill="#fff" />
          <circle cx="65" cy="40" r="10" fill="#fff" />
          <circle cx="35" cy="40" r="4" fill="#000" />
          <circle cx="65" cy="40" r="4" fill="#000" />
          <!-- Mouth -->
          <path d="M 30 65 Q 50 85 70 65" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" />
        </svg>
      </div>
      <div class="cookiegame-card">
        <h4 id="cookie-name">Loading...</h4>
        <p id="cookie-desc">Loading details...</p>
      </div>
      <div class="wifigame-btn-bar">
        <button class="wifigame-btn btn-unsafe" id="cookie-reject"><i class="fa-solid fa-xmark"></i> REJECT</button>
        <button class="wifigame-btn btn-safe" id="cookie-accept"><i class="fa-solid fa-check"></i> ACCEPT</button>
      </div>
    `;
    container.appendChild(wrapper);

    const cookies = [
      { name: "session_id", desc: "Keeps you logged in as you click between page tabs.", essential: true },
      { name: "tracking_ad_pixel", desc: "Builds a passive query path to deliver shoe ads.", essential: false },
      { name: "shopping_cart_token", desc: "Remembers the items inside your cart during checkout.", essential: true },
      { name: "third_party_analytics", desc: "Exposes browser history parameters to marketing partners.", essential: false }
    ];

    let currentIdx = 0;
    let mistakes = 0;

    const loadCookie = () => {
      if (currentIdx >= cookies.length) {
        this.submitGameCompletion({
          level: 12, xp: 100, coins: 20, stars: mistakes === 0 ? 3 : 1,
          correct_count: cookies.length - mistakes, wrong_count: mistakes,
          privacy_diff: 15, security_diff: 5, reputation_diff: 2, trust_diff: 5
        });
        return;
      }
      
      const ck = cookies[currentIdx];
      document.getElementById('cookie-name').textContent = ck.name;
      document.getElementById('cookie-desc').textContent = ck.desc;
    };

    const handleCookie = (accept) => {
      const ck = cookies[currentIdx];
      if (ck.essential === accept) {
        this.updateMascotFace('happy', "Yum! That cookie choice was secure.");
      } else {
        mistakes++;
        this.updateMascotFace('sad', "Ouch! Accepting ad tracking cookies compromises privacy.");
      }
      currentIdx++;
      setTimeout(loadCookie, 700);
    };

    document.getElementById('cookie-reject').addEventListener('click', () => handleCookie(false));
    document.getElementById('cookie-accept').addEventListener('click', () => handleCookie(true));

    loadCookie();
  }

  // 7. App Permission Guard
  setupPermissionGame(container) {
    this.updateMascotFace('neutral', "Review mobile app hardware permissions! Limit access.");
    
    const wrapper = document.createElement('div');
    wrapper.innerHTML = `
      <div class="permgame-screen">
        <div class="permgame-app-header" id="perm-app-title">Flashlight Pro</div>
        <div class="permgame-app-body">
          <p id="perm-app-desc">Flashlight app utility tool.</p>
          
          <div class="permgame-alert-box">
            <div class="permgame-alert-title">Permission Request</div>
            <div class="permgame-alert-desc" id="perm-alert-text">Allow location access?</div>
            <div class="permgame-alert-buttons">
              <button class="permgame-btn btn-allow" id="perm-allow">ALLOW</button>
              <button class="permgame-btn btn-deny" id="perm-deny">DENY</button>
            </div>
          </div>
        </div>
      </div>
    `;
    container.appendChild(wrapper);

    const apps = [
      { name: "Flashlight Pro", desc: "A clean flashlight widget app.", req: "Requires access to GPS location data.", allow: false },
      { name: "City Maps", desc: "Live navigation routing tool.", req: "Requires access to GPS location data.", allow: true },
      { name: "Calculator widget", desc: "Basic arithmetic utility.", req: "Requires access to physical contacts list.", allow: false },
      { name: "Voice Note Maker", desc: "Audio recording memo creator.", req: "Requires access to device microphone.", allow: true }
    ];

    let currentIdx = 0;
    let mistakes = 0;

    const loadApp = () => {
      if (currentIdx >= apps.length) {
        this.submitGameCompletion({
          level: 13, xp: 100, coins: 20, stars: mistakes === 0 ? 3 : 1,
          correct_count: apps.length - mistakes, wrong_count: mistakes,
          privacy_diff: 15, security_diff: 10, reputation_diff: 5, trust_diff: 5
        });
        return;
      }
      
      const app = apps[currentIdx];
      document.getElementById('perm-app-title').textContent = app.name;
      document.getElementById('perm-app-desc').textContent = app.desc;
      document.getElementById('perm-alert-text').textContent = app.req;
    };

    const handleChoice = (allowed) => {
      const app = apps[currentIdx];
      if (app.allow === allowed) {
        this.updateMascotFace('happy', "Correct! Guarding app permissions stops silent data leaks.");
      } else {
        mistakes++;
        this.updateMascotFace('sad', "Incorrect permissions! Deny flashlight GPS requests.");
      }
      currentIdx++;
      setTimeout(loadApp, 800);
    };

    document.getElementById('perm-allow').addEventListener('click', () => handleChoice(true));
    document.getElementById('perm-deny').addEventListener('click', () => handleChoice(false));

    loadApp();
  }

  // 8. Memory Match Card Grid
  setupMatchGame(container) {
    this.updateMascotFace('neutral', "Match the cryptographic password managers concepts!");
    
    const grid = document.createElement('div');
    grid.className = "matchgame-grid";
    container.appendChild(grid);

    // List of match cards (pairs must have matching text codes)
    const items = [
      { id: 1, text: "Vault", pair: "A" },
      { id: 2, text: "Safe Storage", pair: "A" },
      { id: 3, text: "TOTP", pair: "B" },
      { id: 4, text: "Two Factor", pair: "B" },
      { id: 5, text: "Passphrase", pair: "C" },
      { id: 6, text: "Word list", pair: "C" },
      { id: 7, text: "AutoFill", pair: "D" },
      { id: 8, text: "Form Shield", pair: "D" }
    ];

    // Shuffle items array
    items.sort(() => Math.random() - 0.5);

    let activeCards = [];
    let matchedCount = 0;

    items.forEach(item => {
      const card = document.createElement('div');
      card.className = "matchgame-card";
      card.innerHTML = `<span class="matchgame-card-content">${item.text}</span>`;
      
      card.addEventListener('click', () => {
        if (card.classList.contains('flipped') || card.classList.contains('matched') || activeCards.length >= 2) return;
        
        card.classList.add('flipped');
        activeCards.push({ card, item });

        if (activeCards.length === 2) {
          const [c1, c2] = activeCards;
          if (c1.item.pair === c2.item.pair) {
            // Match found!
            c1.card.classList.add('matched');
            c2.card.classList.add('matched');
            c1.card.classList.remove('flipped');
            c2.card.classList.remove('flipped');
            
            activeCards = [];
            matchedCount += 2;
            this.updateMascotFace('happy', "Nice match! Vault connects to Safe Storage.");

            if (matchedCount === items.length) {
              setTimeout(() => {
                this.submitGameCompletion({
                  level: 19, xp: 100, coins: 25, stars: 3, correct_count: 4, wrong_count: 0,
                  privacy_diff: 5, security_diff: 15, reputation_diff: 5, trust_diff: 10
                });
              }, 1000);
            }
          } else {
            // Not a match
            this.updateMascotFace('sad', "Not a match! Try again.");
            setTimeout(() => {
              c1.card.classList.remove('flipped');
              c2.card.classList.remove('flipped');
              activeCards = [];
            }, 1000);
          }
        }
      });
      grid.appendChild(card);
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new GameJourneyMap();
});
