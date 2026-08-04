/**
 * ==========================================================================
 * SPACE BACKGROUND CANVAS ENGINE
 * Stars, Nebula Clouds, Floating Digital Footprints, Shooting Stars
 * ==========================================================================
 */

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
    this.mouse = { x: window.innerWidth / 2, y: window.innerHeight / 2 };

    window.addEventListener('mousemove', (e) => {
      this.mouse.x = e.clientX;
      this.mouse.y = e.clientY;
    });

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
        twinkleSpeed: (Math.random() * 0.02 + 0.005) * (Math.random() < 0.5 ? 1 : -1)
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
    this.ripples.push({ x, y, radius: 0, alpha: 0.8 });
  }

  drawDigitalFootprint(x, y, size, rotation, alpha, color) {
    this.ctx.save();
    this.ctx.translate(x, y);
    this.ctx.rotate(rotation);
    this.ctx.globalAlpha = alpha;
    this.ctx.fillStyle = color;
    this.ctx.shadowBlur = 12;
    this.ctx.shadowColor = color;

    this.ctx.beginPath();
    this.ctx.ellipse(0, 0, size * 0.4, size * 0.7, 0, 0, Math.PI * 2);
    this.ctx.fill();

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

    for (let n of this.nebulaClouds) {
      n.x += n.vx; n.y += n.vy;
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

    for (let s of this.stars) {
      s.alpha += s.twinkleSpeed;
      if (s.alpha <= 0.1 || s.alpha >= 1) s.twinkleSpeed *= -1;

      const dx = this.mouse.x - s.x;
      const dy = this.mouse.y - s.y;
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

    for (let f of this.footprints) {
      f.x += f.vx; f.y += f.vy; f.rotation += f.vRot; f.pulse += 0.03;
      const currentAlpha = f.alpha + Math.sin(f.pulse) * 0.15;
      if (f.y < -50) { f.y = this.height + 50; f.x = Math.random() * this.width; }
      this.drawDigitalFootprint(f.x, f.y, f.size, f.rotation, Math.max(0.1, currentAlpha), f.color);
    }

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
      m.x += m.speed; m.y += m.speed * 0.6; m.alpha -= 0.02;
      if (m.alpha <= 0) { this.meteors.splice(i, 1); continue; }
      const grad = this.ctx.createLinearGradient(m.x, m.y, m.x - m.length, m.y - m.length * 0.6);
      grad.addColorStop(0, `rgba(0, 240, 255, ${m.alpha})`);
      grad.addColorStop(1, 'transparent');
      this.ctx.strokeStyle = grad; this.ctx.lineWidth = 2;
      this.ctx.beginPath(); this.ctx.moveTo(m.x, m.y); this.ctx.lineTo(m.x - m.length, m.y - m.length * 0.6); this.ctx.stroke();
    }

    for (let i = this.ripples.length - 1; i >= 0; i--) {
      const r = this.ripples[i];
      r.radius += 2.5; r.alpha -= 0.02;
      if (r.alpha <= 0) { this.ripples.splice(i, 1); continue; }
      this.ctx.strokeStyle = `rgba(0, 240, 255, ${r.alpha})`;
      this.ctx.lineWidth = 1.5;
      this.ctx.beginPath(); this.ctx.arc(r.x, r.y, r.radius, 0, Math.PI * 2); this.ctx.stroke();
    }

    requestAnimationFrame(() => this.animate());
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new SpaceEngine('space-canvas');
});
