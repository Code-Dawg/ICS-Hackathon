/**
 * ==========================================================================
 * SCROLL REVEALS & BACK TO TOP BUTTON
 * ==========================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  const revealEls = document.querySelectorAll('.reveal-on-scroll');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
      }
    });
  }, { threshold: 0.15 });

  revealEls.forEach(el => observer.observe(el));

  const backBtn = document.querySelector('.back-to-top');
  if (backBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) backBtn.classList.add('visible');
      else backBtn.classList.remove('visible');
    });

    backBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Timeline scroll trigger progress
  const timelineItems = document.querySelectorAll('.timeline-item');
  const progressBar = document.querySelector('.timeline-progress');
  if (timelineItems.length > 0) {
    const itemObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) entry.target.classList.add('active');
      });
    }, { threshold: 0.3 });

    timelineItems.forEach(item => itemObserver.observe(item));

    window.addEventListener('scroll', () => {
      const timelineWrapper = document.querySelector('.timeline-wrapper');
      if (!timelineWrapper || !progressBar) return;
      const rect = timelineWrapper.getBoundingClientRect();
      const winHeight = window.innerHeight;

      if (rect.top < winHeight && rect.bottom > 0) {
        const totalHeight = rect.height;
        const visiblePart = winHeight - rect.top;
        const progressPercent = Math.min(100, Math.max(0, (visiblePart / totalHeight) * 100));
        progressBar.style.height = `${progressPercent}%`;
      }
    });
  }
});
