const DELETE_URL = 'delete-4f3d2a1b-1b3c-4a2b-8c1a-3b2c1a4f3d2a';

// ===== Delete User Modal =====
function openDeleteUserModal(userId, userName) {
    console.log('openDeleteUserModal');
    const user = document.getElementById('user-username');
    user.innerHTML = userName;
    const Form = document.getElementById('delete-user-form');
    Form.action = '/users/' + DELETE_URL + "/" + userId + "/";
    toggleDeleteUserModal();
}

function toggleDeleteUserModal() {
    console.log('toggleDeleteUserModal');
    const modal = document.getElementById('delete-user-modal');
    modal.classList.toggle('show');
}

// ===== Create User Modal =====
function openCreateUserModal() {
  toggleCreateUserModal();
}

function toggleCreateUserModal() {
    const modal = document.getElementById('create-user-modal');
    modal.classList.toggle('show');
}