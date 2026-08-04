/**
 * ==========================================================================
 * GLASSMORPHISM MODALS CONTROLLER
 * Open, close, keyboard shortcuts, backdrop clicks, login/register switching
 * ==========================================================================
 */

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
      btn.addEventListener('click', () => this.closeAllModals());
    });

    document.querySelectorAll('.modal-overlay').forEach(modal => {
      modal.addEventListener('click', (e) => {
        if (e.target === modal) this.closeAllModals();
      });
    });

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.closeAllModals();
    });

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

document.addEventListener('DOMContentLoaded', () => {
  new ModalsController();
});
