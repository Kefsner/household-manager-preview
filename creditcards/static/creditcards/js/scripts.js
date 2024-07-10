// ===== Pay Credit Card Modal =====
function openPayCreditCardModal(creditCardId, creditCardName) {
    const creditCard = document.getElementById('pay-creditcard-name');
    creditCard.innerHTML = creditCardName;
    const Form = document.getElementById('pay-creditcard-form');
    Form.action = `/creditcards/pay/${creditCardId}/`;
    toggleModal('pay-creditcard-modal');
}

function handlePageSpecificFormErrors(field, message) {
    let spanId;
    let pk;
    let id;
    let card_name;
    if (field.endsWith('_pay')) {
      field = field.replace('_pay', '');
      [field, pk] = field.split('_');
      [id, card_name] = pk.split('-');
      spanId = `pay-creditcard-${field}-error`;
      openPayCreditCardModal(pk, card_name);
    } else {
      spanId = `create-creditcard-${field}-error`;
      toggleModal('create-creditcard-modal');
    }
    const span = document.getElementById(spanId);
    span.hidden = false;
    span.innerHTML = message.innerHTML;
    const input = span.closest('.form-element-container').querySelector('input, select');
    input.classList.add('error');
}