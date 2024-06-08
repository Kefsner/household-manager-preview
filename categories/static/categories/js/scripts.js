const DELETE_URL = 'delete-4f3d2a1b-1b3c-4a2b-8c1a-3b2c1a4f3d2a';

// ===== Delete Category Modal =====
function openDeleteCategoryModal(categoryId, categoryName) {
    const category = document.getElementById('category-name');
    category.innerHTML = categoryName;
    const Form = document.getElementById('delete-category-form');
    Form.action = '/categories/' + DELETE_URL + "/" + categoryId + "/";
    toggleDeleteCategoryModal();
}

function toggleDeleteCategoryModal() {
    const modal = document.getElementById('delete-category-modal');
    modal.classList.toggle('show');
}

// ===== Create Category Modal =====
function openCreateCategoryModal() {
  toggleCreateCategoryModal();
}

function toggleCreateCategoryModal() {
  const modal = document.getElementById('create-category-modal');
  modal.classList.toggle('show');
}