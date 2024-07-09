const DELETE_URL = 'delete-4f3d2a1b-1b3c-4a2b-8c1a-3b2c1a4f3d2a';

// ===== Delete Credit Card Modal =====
function openDeleteCreditCardModal(creditCardId, creditCardName) {
    const creditCard = document.getElementById('creditcard-name');
    creditCard.innerHTML = creditCardName;
    const Form = document.getElementById('delete-creditcard-form');
    Form.action = '/creditcards/' + DELETE_URL + "/creditcard/" + creditCardId + "/";
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
  if (modal.classList.contains('show')) {
    const form = modal.querySelector('form');
    form.reset();
    const fields = form.querySelectorAll('input, select');
    fields.forEach(input => {
      input.classList.remove('error');
    });
    const spans = form.querySelectorAll('span');
    spans.forEach(span => {
      span.hidden = true;
      span.innerHTML = '';
    });
  }
  modal.classList.toggle('show');
}

// ===== Pay Credit Card Modal =====
function openPayCreditCardModal(creditCardId, creditCardName) {
    const creditCard = document.getElementById('pay-creditcard-name');
    creditCard.innerHTML = creditCardName;
    const Form = document.getElementById('pay-creditcard-form');
    Form.action = '/creditcards/' + creditCardId + '/pay/';
    togglePayCreditCardModal();
}

function togglePayCreditCardModal() {
    const modal = document.getElementById('pay-creditcard-modal');
    if (modal.classList.contains('show')) {
        const form = modal.querySelector('form');
        form.reset();
        const fields = form.querySelectorAll('input, select');
        fields.forEach(input => {
            input.classList.remove('error');
        });
        const spans = form.querySelectorAll('span');
        spans.forEach(span => {
            span.hidden = true;
            span.innerHTML = '';
        });
    }
    modal.classList.toggle('show');
}

// ===== Auto open form modal if there is an error =====
document.addEventListener('DOMContentLoaded', function () {
  const message = document.querySelector('.message-content');
  const tags = document.querySelector('.message-tags');
  if (message && tags) {
      let [form, field] = tags.innerHTML.split(' ');
      let spanId;
      let pk;
      let id;
      let card_name;
      if (form === 'page') {
        if (field.endsWith('_pay')) {
          field = field.replace('_pay', '');
          [field, pk] = field.split('_');
          [id, card_name] = pk.split('-');
          spanId = `pay-creditcard-${field}-error`;
          openPayCreditCardModal(pk, card_name);
        } else {
          spanId = `create-creditcard-${field}-error`;
          openCreateCreditCardModal();
        }
        const span = document.getElementById(spanId);
        span.hidden = false;
        span.innerHTML = message.innerHTML;
        const input = span.closest('.form-element-container').querySelector('input, select');
        input.classList.add('error');
      }
    }
});