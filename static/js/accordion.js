/**
 * ==========================================================================
 * FAQ ACCORDION
 * Toggle items open/closed smoothly
 * ==========================================================================
 */

class FAQAccordion {
  constructor() {
    this.items = document.querySelectorAll('.faq-item');
    this.init();
  }

  init() {
    this.items.forEach(item => {
      const header = item.querySelector('.faq-header');
      if (!header) return;
      header.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        this.items.forEach(i => i.classList.remove('active'));
        if (!isActive) item.classList.add('active');
      });
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new FAQAccordion();
});
