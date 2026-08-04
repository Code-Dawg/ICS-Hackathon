/**
 * ==========================================================================
 * CUSTOM CURSOR MANAGER
 * Smooth ring and dot lerp with hover interaction styling
 * ==========================================================================
 */

class CustomCursor {
  constructor() {
    this.dot = document.getElementById('cursor-dot');
    this.ring = document.getElementById('cursor-ring');
    if (!this.dot || !this.ring) return;

    this.mouse = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
    this.dotX = 0; this.dotY = 0;
    this.ringX = 0; this.ringY = 0;

    window.addEventListener('mousemove', (e) => {
      this.mouse.x = e.clientX;
      this.mouse.y = e.clientY;
    });

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
    this.dotX += (this.mouse.x - this.dotX) * 0.35;
    this.dotY += (this.mouse.y - this.dotY) * 0.35;
    this.ringX += (this.mouse.x - this.ringX) * 0.15;
    this.ringY += (this.mouse.y - this.ringY) * 0.15;

    this.dot.style.transform = `translate(${this.dotX}px, ${this.dotY}px)`;
    this.ring.style.transform = `translate(${this.ringX}px, ${this.ringY}px)`;

    requestAnimationFrame(() => this.animate());
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new CustomCursor();
});
