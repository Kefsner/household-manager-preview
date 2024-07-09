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
    const modal = document.getElementById('delete-user-modal');
    modal.classList.toggle('show');
}

// ===== Create User Modal =====
function openCreateUserModal() {
  toggleCreateUserModal();
}

function toggleCreateUserModal() {
    const modal = document.getElementById('create-user-modal');
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
    console.log('message:', message);
    console.log('tags:', tags);
    if (message && tags) {
        const [form, field] = tags.innerHTML.split(' ');
        if (form === 'page') {
            const spanId = `create-user-${field}-error`;
            const span = document.getElementById(spanId);
            span.hidden = false;
            span.innerHTML = message.innerHTML;
            const input = span.closest('.form-element-container').querySelector('input, select');
            input.classList.add('error');
            openCreateUserModal();
        }
    }
});