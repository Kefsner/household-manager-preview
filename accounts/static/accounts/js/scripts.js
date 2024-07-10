function handlePageSpecificFormErrors(field, message) {
  const spanId = `create-account-${field}-error`;
  const span = document.getElementById(spanId);
  span.hidden = false;
  span.innerHTML = message.innerHTML;
  const input = span.closest('.form-element-container').querySelector('input, select');
  input.classList.add('error');
  toggleModal('create-account-modal');
}