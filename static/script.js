/**
 * ==========================================================================
 * EDUPULSE / DIGITAL FOOTPRINT - FUTURISTIC INTERACTIVE SCRIPT
 * Space Engine, Eye-Tracking Avatar, Custom Cursor, Modals & Animations
 * ==========================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  // Mouse global state
  const mouse = {
    x: window.innerWidth / 2,
    y: window.innerHeight / 2,
    targetX: window.innerWidth / 2,
    targetY: window.innerHeight / 2,
    isHovered: false
  };

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  /* --------------------------------------------------------------------------
     1. ANIMATED SPACE CANVAS ENGINE (Stars, Nebula, Footprints, Meteors)
     -------------------------------------------------------------------------- */
  class SpaceEngine {
    constructor(canvasId) {
      this.canvas = document.getElementById(canvasId);
      if (!this.canvas) return;
      this.ctx = this.canvas.getContext('2d');
      this.stars = [];
      this.footprints = [];
      this.meteors = [];
      this.nebulaClouds = [];
      this.ripples = [];
      
      this.init();
      this.animate();

      window.addEventListener('resize', () => this.resize());
      window.addEventListener('click', (e) => this.addRipple(e.clientX, e.clientY));
    }

    init() {
      this.resize();
      this.createStars(140);
      this.createFootprints(24);
      this.createNebula(5);
    }

    resize() {
      this.width = this.canvas.width = window.innerWidth;
      this.height = this.canvas.height = window.innerHeight;
    }

    createStars(count) {
      this.stars = [];
      for (let i = 0; i < count; i++) {
        this.stars.push({
          x: Math.random() * this.width,
          y: Math.random() * this.height,
          size: Math.random() * 2 + 0.5,
          alpha: Math.random(),
          twinkleSpeed: (Math.random() * 0.02 + 0.005) * (Math.random() < 0.5 ? 1 : -1),
          layer: Math.random() * 2 + 1
        });
      }
    }

    createFootprints(count) {
      this.footprints = [];
      for (let i = 0; i < count; i++) {
        this.footprints.push({
          x: Math.random() * this.width,
          y: Math.random() * this.height,
          size: Math.random() * 16 + 12,
          vx: (Math.random() - 0.5) * 0.4,
          vy: -Math.random() * 0.5 - 0.2,
          rotation: Math.random() * Math.PI * 2,
          vRot: (Math.random() - 0.5) * 0.01,
          alpha: Math.random() * 0.6 + 0.2,
          pulse: Math.random() * Math.PI,
          color: Math.random() > 0.5 ? '#00f0ff' : '#8b5cf6'
        });
      }
    }

    createNebula(count) {
      this.nebulaClouds = [];
      for (let i = 0; i < count; i++) {
        this.nebulaClouds.push({
          x: Math.random() * this.width,
          y: Math.random() * this.height,
          radius: Math.random() * 250 + 150,
          color: i % 2 === 0 ? 'rgba(0, 240, 255, 0.03)' : 'rgba(139, 92, 246, 0.035)',
          vx: (Math.random() - 0.5) * 0.2,
          vy: (Math.random() - 0.5) * 0.2
        });
      }
    }

    addRipple(x, y) {
      this.ripples.push({
        x, y, radius: 0, maxRadius: 80, alpha: 0.8
      });
    }

    drawDigitalFootprint(x, y, size, rotation, alpha, color) {
      this.ctx.save();
      this.ctx.translate(x, y);
      this.ctx.rotate(rotation);
      this.ctx.globalAlpha = alpha;
      this.ctx.fillStyle = color;
      this.ctx.shadowBlur = 12;
      this.ctx.shadowColor = color;

      // Draw stylized footprint icon (sole + toes)
      this.ctx.beginPath();
      this.ctx.ellipse(0, 0, size * 0.4, size * 0.7, 0, 0, Math.PI * 2);
      this.ctx.fill();

      // Digital circuit toes
      for (let t = 0; t < 4; t++) {
        const angle = -Math.PI / 3 + (t * Math.PI / 4.5);
        const toeX = Math.sin(angle) * (size * 0.65);
        const toeY = -Math.cos(angle) * (size * 0.75);
        this.ctx.beginPath();
        this.ctx.arc(toeX, toeY, size * 0.12, 0, Math.PI * 2);
        this.ctx.fill();
      }

      this.ctx.restore();
    }

    animate() {
      this.ctx.clearRect(0, 0, this.width, this.height);

      // 1. Draw Nebula Clouds
      for (let n of this.nebulaClouds) {
        n.x += n.vx;
        n.y += n.vy;
        if (n.x < -n.radius) n.x = this.width + n.radius;
        if (n.x > this.width + n.radius) n.x = -n.radius;
        if (n.y < -n.radius) n.y = this.height + n.radius;
        if (n.y > this.height + n.radius) n.y = -n.radius;

        const grad = this.ctx.createRadialGradient(n.x, n.y, 0, n.x, n.y, n.radius);
        grad.addColorStop(0, n.color);
        grad.addColorStop(1, 'transparent');
        this.ctx.fillStyle = grad;
        this.ctx.beginPath();
        this.ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
        this.ctx.fill();
      }

      // 2. Draw Stars with Parallax Mouse Push
      for (let s of this.stars) {
        s.alpha += s.twinkleSpeed;
        if (s.alpha <= 0.1 || s.alpha >= 1) s.twinkleSpeed *= -1;

        // Particle reaction to cursor
        const dx = mouse.x - s.x;
        const dy = mouse.y - s.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        let shiftX = 0, shiftY = 0;
        if (dist < 120) {
          const force = (120 - dist) / 120;
          shiftX = -(dx / dist) * force * 15;
          shiftY = -(dy / dist) * force * 15;
        }

        this.ctx.fillStyle = `rgba(255, 255, 255, ${s.alpha})`;
        this.ctx.beginPath();
        this.ctx.arc(s.x + shiftX, s.y + shiftY, s.size, 0, Math.PI * 2);
        this.ctx.fill();
      }

      // 3. Draw Floating Digital Footprints
      for (let f of this.footprints) {
        f.x += f.vx;
        f.y += f.vy;
        f.rotation += f.vRot;
        f.pulse += 0.03;
        const currentAlpha = f.alpha + Math.sin(f.pulse) * 0.15;

        // Respawn if off screen
        if (f.y < -50) {
          f.y = this.height + 50;
          f.x = Math.random() * this.width;
        }

        this.drawDigitalFootprint(f.x, f.y, f.size, f.rotation, Math.max(0.1, currentAlpha), f.color);
      }

      // 4. Random Shooting Star Meteors
      if (Math.random() < 0.02) {
        this.meteors.push({
          x: Math.random() * this.width,
          y: Math.random() * (this.height / 2),
          length: Math.random() * 80 + 50,
          speed: Math.random() * 10 + 8,
          alpha: 1
        });
      }

      for (let i = this.meteors.length - 1; i >= 0; i--) {
        const m = this.meteors[i];
        m.x += m.speed;
        m.y += m.speed * 0.6;
        m.alpha -= 0.02;

        if (m.alpha <= 0) {
          this.meteors.splice(i, 1);
          continue;
        }

        const grad = this.ctx.createLinearGradient(m.x, m.y, m.x - m.length, m.y - m.length * 0.6);
        grad.addColorStop(0, `rgba(0, 240, 255, ${m.alpha})`);
        grad.addColorStop(1, 'transparent');

        this.ctx.strokeStyle = grad;
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.moveTo(m.x, m.y);
        this.ctx.lineTo(m.x - m.length, m.y - m.length * 0.6);
        this.ctx.stroke();
      }

      // 5. Draw Mouse Click Ripples
      for (let i = this.ripples.length - 1; i >= 0; i--) {
        const r = this.ripples[i];
        r.radius += 2.5;
        r.alpha -= 0.02;
        if (r.alpha <= 0) {
          this.ripples.splice(i, 1);
          continue;
        }
        this.ctx.strokeStyle = `rgba(0, 240, 255, ${r.alpha})`;
        this.ctx.lineWidth = 1.5;
        this.ctx.beginPath();
        this.ctx.arc(r.x, r.y, r.radius, 0, Math.PI * 2);
        this.ctx.stroke();
      }

      requestAnimationFrame(() => this.animate());
    }
  }

  /* --------------------------------------------------------------------------
     2. EYE-TRACKING & DIGITAL HUMAN CYBER AVATAR PHYSICS
     -------------------------------------------------------------------------- */
  class CyberAvatar {
    constructor() {
      this.leftPupil = document.getElementById('left-pupil');
      this.rightPupil = document.getElementById('right-pupil');
      this.avatarHead = document.getElementById('avatar-head');
      this.eyelids = document.querySelectorAll('.eye-lid');
      this.avatarContainer = document.querySelector('.avatar-container');

      if (!this.leftPupil || !this.rightPupil) return;

      this.currentX = 0;
      this.currentY = 0;
      this.targetX = 0;
      this.targetY = 0;

      this.initEvents();
      this.initBlinking();
      this.updatePhysics();
    }

    initEvents() {
      window.addEventListener('mousemove', (e) => {
        if (!this.avatarContainer) return;
        const rect = this.avatarContainer.getBoundingClientRect();
        const centerX = rect.left + rect.width / 2;
        const centerY = rect.top + rect.height / 2;

        const deltaX = e.clientX - centerX;
        const deltaY = e.clientY - centerY;
        const dist = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
        const angle = Math.atan2(deltaY, deltaX);

        // Limit pupil rotation to realistic eye socket bounds (max 16px radius)
        const maxRadius = 16;
        const clampedDist = Math.min(dist * 0.08, maxRadius);

        this.targetX = Math.cos(angle) * clampedDist;
        this.targetY = Math.sin(angle) * clampedDist;

        // Calculate head tilt (max 5 deg)
        this.headTiltX = Math.max(-5, Math.min(5, (e.clientX - window.innerWidth / 2) * 0.01));
        this.headTiltY = Math.max(-4, Math.min(4, (e.clientY - window.innerHeight / 2) * 0.01));
      });

      document.addEventListener('mouseleave', () => {
        this.targetX = 0;
        this.targetY = 0;
        this.headTiltX = 0;
        this.headTiltY = 0;
      });
    }

    initBlinking() {
      const blink = () => {
        this.eyelids.forEach(el => el.classList.add('blinking'));
        setTimeout(() => {
          this.eyelids.forEach(el => el.classList.remove('blinking'));
        }, 150);

        // Random double-blink
        if (Math.random() < 0.25) {
          setTimeout(() => {
            this.eyelids.forEach(el => el.classList.add('blinking'));
            setTimeout(() => {
              this.eyelids.forEach(el => el.classList.remove('blinking'));
            }, 140);
          }, 300);
        }

        const nextBlink = Math.random() * 3500 + 2500;
        setTimeout(blink, nextBlink);
      };
      setTimeout(blink, 3000);
    }

    updatePhysics() {
      // Lerp pupil position for smooth physical movement
      this.currentX += (this.targetX - this.currentX) * 0.12;
      this.currentY += (this.targetY - this.currentY) * 0.12;

      if (this.leftPupil && this.rightPupil) {
        this.leftPupil.setAttribute('transform', `translate(${this.currentX}, ${this.currentY})`);
        this.rightPupil.setAttribute('transform', `translate(${this.currentX}, ${this.currentY})`);
      }

      if (this.avatarHead) {
        const tiltX = this.headTiltX || 0;
        const tiltY = this.headTiltY || 0;
        this.avatarHead.style.transform = `rotate(${tiltX}deg) translate(${tiltX * 1.5}px, ${tiltY * 1.5}px)`;
      }

      requestAnimationFrame(() => this.updatePhysics());
    }
  }

  /* --------------------------------------------------------------------------
     3. CUSTOM CURSOR MANAGER WITH MAGNETIC BUTTON ATTRACTION
     -------------------------------------------------------------------------- */
  class CustomCursor {
    constructor() {
      this.dot = document.getElementById('cursor-dot');
      this.ring = document.getElementById('cursor-ring');
      if (!this.dot || !this.ring) return;

      this.dotX = 0;
      this.dotY = 0;
      this.ringX = 0;
      this.ringY = 0;

      this.initHoverStates();
      this.animate();
    }

    initHoverStates() {
      const interactiveEls = document.querySelectorAll('a, button, .btn, .interactive, .faq-header, .tilt-card');
      interactiveEls.forEach(el => {
        el.addEventListener('mouseenter', () => this.ring.classList.add('active'));
        el.addEventListener('mouseleave', () => this.ring.classList.remove('active'));
      });
    }

    animate() {
      this.dotX += (mouse.x - this.dotX) * 0.35;
      this.dotY += (mouse.y - this.dotY) * 0.35;
      this.ringX += (mouse.x - this.ringX) * 0.15;
      this.ringY += (mouse.y - this.ringY) * 0.15;

      this.dot.style.transform = `translate(${this.dotX}px, ${this.dotY}px)`;
      this.ring.style.transform = `translate(${this.ringX}px, ${this.ringY}px)`;

      requestAnimationFrame(() => this.animate());
    }
  }

  /* --------------------------------------------------------------------------
     4. NAVBAR & THEME CONTROLLER
     -------------------------------------------------------------------------- */
  class NavbarController {
    constructor() {
      this.header = document.querySelector('header');
      this.scrollProgress = document.getElementById('scroll-progress');
      this.themeBtn = document.getElementById('theme-toggle');
      this.hamburger = document.getElementById('hamburger');
      this.navLinks = document.querySelector('.nav-links');

      this.initScroll();
      this.initTheme();
      this.initMobileMenu();
    }

    initScroll() {
      window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = (scrollY / docHeight) * 100;

        if (this.scrollProgress) {
          this.scrollProgress.style.width = `${progress}%`;
        }

        if (this.header) {
          if (scrollY > 40) {
            this.header.classList.add('scrolled');
          } else {
            this.header.classList.remove('scrolled');
          }
        }
      });
    }

    initTheme() {
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme === 'light') {
        document.body.classList.add('light-theme');
      }

      if (this.themeBtn) {
        this.themeBtn.addEventListener('click', () => {
          document.body.classList.toggle('light-theme');
          const isLight = document.body.classList.contains('light-theme');
          localStorage.setItem('theme', isLight ? 'light' : 'dark');
        });
      }
    }

    initMobileMenu() {
      if (this.hamburger && this.navLinks) {
        this.hamburger.addEventListener('click', () => {
          this.hamburger.classList.toggle('active');
          this.navLinks.classList.toggle('active');
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-link').forEach(link => {
          link.addEventListener('click', () => {
            this.hamburger.classList.remove('active');
            this.navLinks.classList.remove('active');
          });
        });
      }
    }
  }

  /* --------------------------------------------------------------------------
     5. MODALS CONTROLLER (LOGIN & REGISTER)
     -------------------------------------------------------------------------- */
  class ModalsController {
    constructor() {
      this.loginModal = document.getElementById('login-modal');
      this.registerModal = document.getElementById('register-modal');
      this.openLoginBtns = document.querySelectorAll('.open-login');
      this.openRegisterBtns = document.querySelectorAll('.open-register');
      this.closeBtns = document.querySelectorAll('.modal-close');
      this.switchLinks = document.querySelectorAll('.modal-switch');

      this.initEvents();
    }

    initEvents() {
      this.openLoginBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          this.openModal(this.loginModal);
        });
      });

      this.openRegisterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          this.openModal(this.registerModal);
        });
      });

      this.closeBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          this.closeAllModals();
        });
      });

      document.querySelectorAll('.modal-overlay').forEach(modal => {
        modal.addEventListener('click', (e) => {
          if (e.target === modal) this.closeAllModals();
        });
      });

      window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') this.closeAllModals();
      });

      // Switching between login & register
      this.switchLinks.forEach(link => {
        link.addEventListener('click', (e) => {
          e.preventDefault();
          const target = link.dataset.target;
          this.closeAllModals();
          if (target === 'register') this.openModal(this.registerModal);
          if (target === 'login') this.openModal(this.loginModal);
        });
      });
    }

    openModal(modal) {
      if (!modal) return;
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    closeAllModals() {
      document.querySelectorAll('.modal-overlay').forEach(modal => modal.classList.remove('active'));
      document.body.style.overflow = '';
    }
  }

  /* --------------------------------------------------------------------------
     6. STATS ANIMATED COUNTER
     -------------------------------------------------------------------------- */
  class StatsCounter {
    constructor() {
      this.statElements = document.querySelectorAll('.stat-number');
      this.initObserver();
    }

    initObserver() {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            this.animateCounter(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.5 });

      this.statElements.forEach(el => observer.observe(el));
    }

    animateCounter(el) {
      const target = parseInt(el.dataset.count, 10);
      const suffix = el.dataset.suffix || '';
      const duration = 2000;
      const stepTime = 20;
      const steps = duration / stepTime;
      const increment = target / steps;
      let current = 0;

      const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
          current = target;
          clearInterval(timer);
        }
        el.innerText = Math.floor(current).toLocaleString() + suffix;
      }, stepTime);
    }
  }

  /* --------------------------------------------------------------------------
     7. TIMELINE SCROLL TRIGGER & REVEALS
     -------------------------------------------------------------------------- */
  class TimelineController {
    constructor() {
      this.timelineItems = document.querySelectorAll('.timeline-item');
      this.progressBar = document.querySelector('.timeline-progress');
      this.initObserver();
    }

    initObserver() {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('active');
          }
        });
      }, { threshold: 0.3 });

      this.timelineItems.forEach(item => observer.observe(item));

      window.addEventListener('scroll', () => {
        const timelineWrapper = document.querySelector('.timeline-wrapper');
        if (!timelineWrapper || !this.progressBar) return;
        const rect = timelineWrapper.getBoundingClientRect();
        const winHeight = window.innerHeight;

        if (rect.top < winHeight && rect.bottom > 0) {
          const totalHeight = rect.height;
          const visiblePart = winHeight - rect.top;
          const progressPercent = Math.min(100, Math.max(0, (visiblePart / totalHeight) * 100));
          this.progressBar.style.height = `${progressPercent}%`;
        }
      });
    }
  }

  /* --------------------------------------------------------------------------
     8. 3D PARALLAX TILT CARDS
     -------------------------------------------------------------------------- */
  class TiltCards {
    constructor() {
      this.cards = document.querySelectorAll('.tilt-card, .footprint-card');
      this.init();
    }

    init() {
      this.cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;

          const centerX = rect.width / 2;
          const centerY = rect.height / 2;

          const rotateX = ((y - centerY) / centerY) * -10;
          const rotateY = ((x - centerX) / centerX) * 10;

          card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        });

        card.addEventListener('mouseleave', () => {
          card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
        });
      });
    }
  }

  /* --------------------------------------------------------------------------
     9. TESTIMONIALS CAROUSEL
     -------------------------------------------------------------------------- */
  class TestimonialCarousel {
    constructor() {
      this.track = document.querySelector('.testimonial-track');
      this.slides = document.querySelectorAll('.testimonial-slide');
      this.prevBtn = document.querySelector('.prev-btn');
      this.nextBtn = document.querySelector('.next-btn');

      if (!this.track || this.slides.length === 0) return;

      this.currentIndex = 0;
      this.init();
    }

    init() {
      if (this.nextBtn) {
        this.nextBtn.addEventListener('click', () => this.next());
      }
      if (this.prevBtn) {
        this.prevBtn.addEventListener('click', () => this.prev());
      }

      // Autoplay every 5 seconds
      setInterval(() => this.next(), 5000);
    }

    update() {
      const offset = -this.currentIndex * 100;
      this.track.style.transform = `translateX(${offset}%)`;
    }

    next() {
      this.currentIndex = (this.currentIndex + 1) % this.slides.length;
      this.update();
    }

    prev() {
      this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
      this.update();
    }
  }

  /* --------------------------------------------------------------------------
     10. FAQ ACCORDION
     -------------------------------------------------------------------------- */
  class FAQAccordion {
    constructor() {
      this.items = document.querySelectorAll('.faq-item');
      this.init();
    }

    init() {
      this.items.forEach(item => {
        const header = item.querySelector('.faq-header');
        header.addEventListener('click', () => {
          const isActive = item.classList.contains('active');
          this.items.forEach(i => i.classList.remove('active'));
          if (!isActive) item.classList.add('active');
        });
      });
    }
  }

  /* --------------------------------------------------------------------------
     11. BUTTON RIPPLE EFFECT & SCROLL REVEALS
     -------------------------------------------------------------------------- */
  function initRippleEffect() {
    document.querySelectorAll('.btn').forEach(button => {
      button.addEventListener('click', function(e) {
        const rect = button.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;

        button.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);
      });
    });
  }

  function initScrollReveals() {
    const revealEls = document.querySelectorAll('.reveal-on-scroll');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
        }
      });
    }, { threshold: 0.15 });

    revealEls.forEach(el => observer.observe(el));
  }

  function initBackToTop() {
    const backBtn = document.querySelector('.back-to-top');
    if (!backBtn) return;

    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backBtn.classList.add('visible');
      } else {
        backBtn.classList.remove('visible');
      }
    });

    backBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Initialize All Systems
  new SpaceEngine('space-canvas');
  new CyberAvatar();
  new CustomCursor();
  new NavbarController();
  new ModalsController();
  new StatsCounter();
  new TimelineController();
  new TiltCards();
  new TestimonialCarousel();
  new FAQAccordion();
  initRippleEffect();
  initScrollReveals();
  initBackToTop();
});
