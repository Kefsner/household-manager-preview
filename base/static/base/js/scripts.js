// ===== Create Transaction Modal =====
function openTransactionModal(type) {
    toggleOpenModelButton();
    toggleTransactionModal(type);
}

function toggleTransactionModal(type) {
    const modal = document.getElementById(type + "-form-container");
    modal.classList.toggle('show');
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