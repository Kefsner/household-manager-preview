const DELETE_URL = 'delete-4f3d2a1b-1b3c-4a2b-8c1a-3b2c1a4f3d2a';

// ===== Delete Account Modal =====
function openDeleteAccountModal(accountId, accountName) {
    const account = document.getElementById('account-name');
    account.innerHTML = accountName;
    const Form = document.getElementById('delete-account-form');
    Form.action = '/accounts/' + DELETE_URL + "/" + accountId + "/";
    toggleDeleteAccountModal();
}

function toggleDeleteAccountModal() {
    const modal = document.getElementById('delete-account-modal');
    modal.classList.toggle('show');
}

// ===== Create Account Modal =====
function openCreateAccountModal() {
  toggleCreateAccountModal();
}

function toggleCreateAccountModal() {
  const modal = document.getElementById('create-account-modal');
  modal.classList.toggle('show');
}
