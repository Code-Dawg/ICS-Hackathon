/**
 * ==========================================================================
 * TESTIMONIALS CAROUSEL
 * Prev/next slide navigation with auto-play interval
 * ==========================================================================
 */

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
    if (this.nextBtn) this.nextBtn.addEventListener('click', () => this.next());
    if (this.prevBtn) this.prevBtn.addEventListener('click', () => this.prev());
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

document.addEventListener('DOMContentLoaded', () => {
  new TestimonialCarousel();
});
