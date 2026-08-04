/**
 * ==========================================================================
 * STATS COUNTER ANIMATION
 * IntersectionObserver count-up numbers
 * ==========================================================================
 */

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

document.addEventListener('DOMContentLoaded', () => {
  new StatsCounter();
});
