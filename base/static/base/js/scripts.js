// ===== Create Transaction Modal =====
function openTransactionModal(type) {
    toggleTransactionModal(type);
}

function toggleTransactionModal(type) {
    const modal = document.getElementById(type + "-form-container");
    modal.classList.toggle('show');
}

document.addEventListener('DOMContentLoaded', function() {
    function updateSubcategories(categorySelect, subcategorySelect, subcategoryOptions) {
        var selectedCategory = categorySelect.value;

        subcategoryOptions.forEach(function(option) {
            if (option.classList.contains('category-' + selectedCategory)) {
                option.style.display = 'block';
            } else {
                option.style.display = 'none';
            }
        });

        // Reset the subcategory select to the default option
        subcategorySelect.value = '';
    }

    var categoryContainers = document.querySelectorAll('.category-container');

    categoryContainers.forEach(function(container) {
        var categorySelect = container.querySelectorAll('select')[0];
        var subcategorySelect = container.querySelectorAll('select')[1];
        var subcategoryOptions = Array.from(subcategorySelect.querySelectorAll('option'));

        // Initialize subcategory options visibility on page load
        updateSubcategories(categorySelect, subcategorySelect, subcategoryOptions);

        categorySelect.addEventListener('change', function() {
            updateSubcategories(categorySelect, subcategorySelect, subcategoryOptions);
        });
    });
});
