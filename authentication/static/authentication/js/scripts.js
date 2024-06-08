const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');
const isRegistration = document.getElementById('isRegistration');

function toggleForm() {
    loginForm.classList.toggle('hidden-form');
    registerForm.classList.toggle('hidden-form');
}