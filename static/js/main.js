/* ==========================================================================
   Digital Footprint Educational Game - Interactive Vanilla JavaScript
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {
    // 1. Choice Selection Handling
    const choiceCards = document.querySelectorAll('.choice-card');
    const submitBtn = document.getElementById('submit-choice-btn');

    if (choiceCards.length > 0) {
        choiceCards.forEach((card, index) => {
            const radio = card.querySelector('input[type="radio"]');

            card.addEventListener('click', function () {
                // Unselect all cards
                choiceCards.forEach(c => c.classList.remove('selected'));
                
                // Select clicked card
                card.classList.add('selected');
                if (radio) {
                    radio.checked = true;
                }

                // Enable submit button
                if (submitBtn) {
                    submitBtn.removeAttribute('disabled');
                    submitBtn.classList.remove('opacity-50');
                }
            });
        });

        // 2. Keyboard Navigation for Scenarios (Press 1, 2, 3, 4)
        document.addEventListener('keydown', function (e) {
            const keyNum = parseInt(e.key);
            if (!isNaN(keyNum) && keyNum >= 1 && keyNum <= choiceCards.length) {
                const targetCard = choiceCards[keyNum - 1];
                if (targetCard) {
                    targetCard.click();
                }
            }
        });
    }

    // 3. Score Counter Animation
    const scoreElements = document.querySelectorAll('.animate-score');
    scoreElements.forEach(el => {
        const targetValue = parseInt(el.getAttribute('data-target') || '0');
        let currentValue = 0;
        const duration = 1000;
        const stepTime = 30;
        const steps = duration / stepTime;
        const increment = targetValue / steps;

        const timer = setInterval(() => {
            currentValue += increment;
            if ((increment >= 0 && currentValue >= targetValue) || (increment < 0 && currentValue <= targetValue)) {
                el.textContent = targetValue;
                clearInterval(timer);
            } else {
                el.textContent = Math.round(currentValue);
            }
        }, stepTime);
    });

    // 4. Auto-dismiss Bootstrap Alerts after 5s
    setTimeout(() => {
        const alerts = document.querySelectorAll('.alert-dismissible');
        alerts.forEach(alert => {
            if (typeof bootstrap !== 'undefined' && bootstrap.Alert) {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            } else {
                alert.style.display = 'none';
            }
        });
    }, 5000);
});
