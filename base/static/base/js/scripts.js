// ===== Create Transaction Modal =====
function openTransactionModal(type) {
    toggleTransactionModal(type);
}

function toggleTransactionModal(type) {
    const modal = document.getElementById(type + "-form-container");
    modal.classList.toggle('show');
}