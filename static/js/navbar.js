/**
 * ==========================================================================
 * GLASS NAVBAR & THEME CONTROLLER
 * Scroll backdrop blur, reading progress, mobile menu, dark/light theme
 * ==========================================================================
 */

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

      if (this.scrollProgress) this.scrollProgress.style.width = `${progress}%`;

      if (this.header) {
        if (scrollY > 40) this.header.classList.add('scrolled');
        else this.header.classList.remove('scrolled');
      }
    });
  }

  initTheme() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') document.body.classList.add('light-theme');

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

      document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
          this.hamburger.classList.remove('active');
          this.navLinks.classList.remove('active');
        });
      });
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  new NavbarController();
});
