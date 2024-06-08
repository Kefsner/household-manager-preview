// ===== Create Transaction Modal =====
function openCreateTransactionModal() {
    toggleCreateTransactionModal();
}

function toggleCreateTransactionModal() {
    const modal = document.getElementById('create-transaction-modal');
    modal.classList.toggle('show');
}