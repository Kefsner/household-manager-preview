// ===== Create Transaction Modal =====
function openTransactionModal(type) {
    toggleOpenModelButton();
    toggleTransactionModal(type);
}

function toggleTransactionModal(type) {
    const modal = document.getElementById(type + "-form-container");
    modal.classList.toggle('show');
}

function toggleOpenModelButton() {
    const modalButtons = document.querySelector('#transaction-modal');
    modalButtons.classList.toggle('show');
    const circleButton = document.querySelector('#circle-button');
    if (circleButton.innerHTML === '+') {
        circleButton.innerHTML = '-';
        circleButton.classList.add('active');
    } else {
        circleButton.innerHTML = '+';
        circleButton.classList.remove('active');
    }
}

// TODO: Add a function for updating the subcategory dropdown based on the selected category