/**
 * ==========================================================================
 * FOOTPRINT QUEST MASCOT - EYE TRACKING & BLINKING PHYSICS
 * Controls the cute mascot head's large glowing white eyes and pupils
 * ==========================================================================
 */

class CuteMascotAvatar {
  constructor() {
    this.leftPupil = document.getElementById('mascot-left-pupil');
    this.rightPupil = document.getElementById('mascot-right-pupil');
    this.mascotHead = document.getElementById('mascot-head');
    this.eyelids = document.querySelectorAll('.mascot-eyelid');
    this.mascotContainer = document.querySelector('.mascot-container');

    if (!this.leftPupil || !this.rightPupil) return;

    this.currentX = 0; this.currentY = 0;
    this.targetX = 0; this.targetY = 0;

    this.initEvents();
    this.initBlinking();
    this.updatePhysics();
  }

  initEvents() {
    window.addEventListener('mousemove', (e) => {
      if (!this.mascotContainer) return;
      const rect = this.mascotContainer.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;

      const deltaX = e.clientX - centerX;
      const deltaY = e.clientY - centerY;
      const dist = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
      const angle = Math.atan2(deltaY, deltaX);

      // Max pupil movement radius for cute mascot eyes
      const maxRadius = 14;
      const clampedDist = Math.min(dist * 0.06, maxRadius);

      this.targetX = Math.cos(angle) * clampedDist;
      this.targetY = Math.sin(angle) * clampedDist;

      // Slight head tilt (max 6 deg)
      this.headTiltX = Math.max(-6, Math.min(6, (e.clientX - window.innerWidth / 2) * 0.012));
      this.headTiltY = Math.max(-5, Math.min(5, (e.clientY - window.innerHeight / 2) * 0.012));
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
      }, 140);

      // Cute double blink occasionally
      if (Math.random() < 0.3) {
        setTimeout(() => {
          this.eyelids.forEach(el => el.classList.add('blinking'));
          setTimeout(() => {
            this.eyelids.forEach(el => el.classList.remove('blinking'));
          }, 120);
        }, 280);
      }

      setTimeout(blink, Math.random() * 3200 + 2200);
    };
    setTimeout(blink, 2500);
  }

  updatePhysics() {
    this.currentX += (this.targetX - this.currentX) * 0.14;
    this.currentY += (this.targetY - this.currentY) * 0.14;

    if (this.leftPupil && this.rightPupil) {
      this.leftPupil.setAttribute('transform', `translate(${this.currentX}, ${this.currentY})`);
      this.rightPupil.setAttribute('transform', `translate(${this.currentX}, ${this.currentY})`);
    }

    if (this.mascotHead) {
      const tiltX = this.headTiltX || 0;
      const tiltY = this.headTiltY || 0;
      this.mascotHead.style.transform = `rotate(${tiltX}deg) translate(${tiltX * 1.2}px, ${tiltY * 1.2}px)`;
    }

    requestAnimationFrame(() => this.updatePhysics());
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new CuteMascotAvatar();
});
