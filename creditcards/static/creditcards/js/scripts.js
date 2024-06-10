const DELETE_URL = 'delete-4f3d2a1b-1b3c-4a2b-8c1a-3b2c1a4f3d2a';

// ===== Delete Credit Card Modal =====
function openDeleteCreditCardModal(creditCardId, creditCardName) {
    const creditCard = document.getElementById('creditcard-name');
    creditCard.innerHTML = creditCardName;
    const Form = document.getElementById('delete-creditcard-form');
    Form.action = '/creditcards/' + DELETE_URL + "/" + creditCardId + "/";
    toggleDeleteCreditCardModal();
}

function toggleDeleteCreditCardModal() {
    const modal = document.getElementById('delete-creditcard-modal');
    modal.classList.toggle('show');
}

// ===== Create Credit Card Modal =====
function openCreateCreditCardModal() {
  toggleCreateCreditCardModal();
}

function toggleCreateCreditCardModal() {
  const modal = document.getElementById('create-creditcard-modal');
  modal.classList.toggle('show');
}