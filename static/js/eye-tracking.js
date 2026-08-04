/**
 * ==========================================================================
 * EYE-TRACKING & CYBER AVATAR PHYSICS
 * Pupils follow cursor position with clamped rotation and head tilt
 * ==========================================================================
 */

class CyberAvatar {
  constructor() {
    this.leftPupil = document.getElementById('left-pupil');
    this.rightPupil = document.getElementById('right-pupil');
    this.avatarHead = document.getElementById('avatar-head');
    this.eyelids = document.querySelectorAll('.eye-lid');
    this.avatarContainer = document.querySelector('.avatar-container');

    if (!this.leftPupil || !this.rightPupil) return;

    this.currentX = 0; this.currentY = 0;
    this.targetX = 0; this.targetY = 0;

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

      const maxRadius = 16;
      const clampedDist = Math.min(dist * 0.08, maxRadius);

      this.targetX = Math.cos(angle) * clampedDist;
      this.targetY = Math.sin(angle) * clampedDist;

      this.headTiltX = Math.max(-5, Math.min(5, (e.clientX - window.innerWidth / 2) * 0.01));
      this.headTiltY = Math.max(-4, Math.min(4, (e.clientY - window.innerHeight / 2) * 0.01));
    });

    document.addEventListener('mouseleave', () => {
      this.targetX = 0; this.targetY = 0;
      this.headTiltX = 0; this.headTiltY = 0;
    });
  }

  initBlinking() {
    const blink = () => {
      this.eyelids.forEach(el => el.classList.add('blinking'));
      setTimeout(() => {
        this.eyelids.forEach(el => el.classList.remove('blinking'));
      }, 150);

      if (Math.random() < 0.25) {
        setTimeout(() => {
          this.eyelids.forEach(el => el.classList.add('blinking'));
          setTimeout(() => {
            this.eyelids.forEach(el => el.classList.remove('blinking'));
          }, 140);
        }, 300);
      }

      setTimeout(blink, Math.random() * 3500 + 2500);
    };
    setTimeout(blink, 3000);
  }

  updatePhysics() {
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

document.addEventListener('DOMContentLoaded', () => {
  new CyberAvatar();
});
