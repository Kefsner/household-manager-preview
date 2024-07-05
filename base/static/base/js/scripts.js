// ===== Create Transaction Modal =====
function openTransactionModal(type) {
    toggleOpenModelButton();
    toggleTransactionModal(type);
}

function toggleTransactionModal(type) {
    const modal = document.getElementById(type + "-form-container");
    modal.classList.toggle('show');
    // Add current url as a field in the form
    const currentUrl = window.location.href;
    const form = modal.querySelector('form');
    const urlInput = document.createElement('input');
    urlInput.type = 'hidden';
    urlInput.name = 'url';
    urlInput.value = currentUrl;
    form.appendChild(urlInput);
}

function toggleOpenModelButton() {
    const modalButtons = document.querySelector('#transaction-modal');
    modalButtons.classList.toggle('show');
    const circleButton = document.querySelector('#circle-button');
    if (circleButton.innerHTML === '+') {
        circleButton.innerHTML = '-';
        circleButton.classList.add('active');
    } else {
        circleButton.innerHTML = '+';
        circleButton.classList.remove('active');
    }
}


// ===== Auto update subcategories based on the selected category =====
document.addEventListener('DOMContentLoaded', function () {
    const categoryDropdowns = document.querySelectorAll('.category-dropdown');
    const subcategoryDropdowns = document.querySelectorAll('.subcategory-dropdown');

    subcategoryDropdowns.forEach((subcategoryDropdown) => {
        const subcategoryOptions = subcategoryDropdown.options;
        Array.from(subcategoryOptions).forEach((option) => {
            option.hidden = true;
        });
    });

    categoryDropdowns.forEach((categoryDropdown, index) => {
        categoryDropdown.addEventListener('change', function () {
            const selectedCategoryId = categoryDropdown.value;
            const subcategoryDropdown = subcategoryDropdowns[index];
            const subcategoryOptions = subcategoryDropdown.options;
            Array.from(subcategoryOptions).forEach((option) => {
                if (option.classList.contains(`category-${selectedCategoryId}`)) {
                    option.hidden = false;
                } else {
                    option.hidden = true;
                }
            });

            subcategoryDropdown.value = '';
        });
    });
});

// ===== Auto update to_account based on the selected from_account =====
document.addEventListener('DOMContentLoaded', function () {
    const accountDropdowns = document.getElementById('transfer-account')
    const toAccountDropdown = document.getElementById('transfer-to_account')

    // Clear options from the to_account dropdown
    const toAccountOptions = toAccountDropdown.options;
    Array.from(toAccountOptions).forEach((option) => {
        option.hidden = true;
    });

    accountDropdowns.addEventListener('change', function () {
        const selectedAccountId = accountDropdowns.value;
        const toAccountOptions = toAccountDropdown.options;
        // Remove the selected account from the to_account dropdown
        Array.from(toAccountOptions).forEach((option) => {
            if (option.value === selectedAccountId) {
                option.hidden = true;
            } else if (option.value === '') {
                option.hidden = true;
            } else {
                option.hidden = false;
            }
        });

        toAccountDropdown.value = '';
    });
});

// ===== Auto open form if form_erros is present =====
document.addEventListener('DOMContentLoaded', function () {
    const formErrors = document.getElementById('form-errors');
    if (formErrors.innerHTML !== '') {
        console.log('Form errors found');
        const type = formErrors.getAttribute('formType');
        toggleTransactionModal(type);
    }
});