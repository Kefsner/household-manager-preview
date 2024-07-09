const DELETE_URL = 'delete-4f3d2a1b-1b3c-4a2b-8c1a-3b2c1a4f3d2a';

// ===== Create Category Modal =====
function openCreateCategoryModal() {
  toggleCreateCategoryModal();
}

function toggleCreateCategoryModal() {
  const modal = document.getElementById('create-category-modal');
  if (modal.classList.contains('show')) {
    const form = modal.querySelector('form');
    form.reset();
    const spans = form.querySelectorAll('span');
    spans.forEach(span => {
      span.hidden = true;
      span.innerHTML = '';
    });
  }
  modal.classList.toggle('show');
}

// ===== Delete Category Modal =====
function openDeleteCategoryModal(categoryId, categoryName) {
    const category = document.getElementById('category-name');
    category.innerHTML = categoryName;
    const Form = document.getElementById('delete-category-form');
    Form.action = '/categories/' + DELETE_URL + "/category/" + categoryId + "/";
    toggleDeleteCategoryModal();
}

function toggleDeleteCategoryModal() {
    const modal = document.getElementById('delete-category-modal');
    modal.classList.toggle('show');
}

// ===== Create Subcategory Modal =====
function openCreateSubcategoryModal(categoryId, categoryName) {
    const category = document.getElementById('subcategory-category-name');
    category.innerHTML = categoryName;
    const Form = document.getElementById('create-subcategory-form');
    Form.action = '/categories/' + categoryId + '/create-subcategory/';
    toggleCreateSubcategoryModal();
}

function toggleCreateSubcategoryModal() {
  const modal = document.getElementById('create-subcategory-modal');
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

// ===== Delete Subcategory Modal =====
function openDeleteSubcategoryModal(subcategoryId, subcategoryName) {
    const subcategory = document.getElementById('subcategory-name');
    subcategory.innerHTML = subcategoryName;
    const Form = document.getElementById('delete-subcategory-form');
    Form.action = '/categories/' + DELETE_URL + "/subcategory/" + subcategoryId + "/";
    toggleDeleteSubcategoryModal();
}

function toggleDeleteSubcategoryModal() {
    const modal = document.getElementById('delete-subcategory-modal');
    modal.classList.toggle('show');
}

// ===== Create Default Category Modal =====
function openCreateDefaultCategoriesModal() {
  toggleCreateDefaultCategoriesModal();
}

function toggleCreateDefaultCategoriesModal() {
  const modal = document.getElementById('create-default-categories-modal');
  modal.classList.toggle('show');
}

// ===== Toggle Subcategories table =====
function toggleSubcategories(categoryId) {
    const subcategories = document.getElementById(categoryId);
    subcategories.classList.toggle('show');
}

// ===== Expand All Subcategories tables =====
function expandAllSubcategories() {
    const subcategories = document.querySelectorAll('.subcategory-table');
    subcategories.forEach((subcategory) => {
        subcategory.classList.add('show');
    });
}

// ===== Collapse All Subcategories tables =====
function collapseAllSubcategories() {
    const subcategories = document.querySelectorAll('.subcategory-table');
    subcategories.forEach((subcategory) => {
        subcategory.classList.remove('show');
    });
}

// ===== Auto open form modal if there is an error =====
document.addEventListener('DOMContentLoaded', function () {
  const message = document.querySelector('.message-content');
  const tags = document.querySelector('.message-tags');
  if (message && tags) {
      let [form, field] = tags.innerHTML.split(' ');
      if (form === 'page') {
        let spanId;
        let pk;
        let id;
        let cat_name;
        if (field.endsWith('_subcategory')) {
          field = field.replace('_subcategory', '');
          [field, pk] = field.split('_');
          [id, cat_name] = pk.split('-');
          spanId = `create-subcategory-${field}-error`;
          openCreateSubcategoryModal(id, cat_name);
        } else {
          spanId = `create-category-${field}-error`;
          openCreateCategoryModal();
        }
        const span = document.getElementById(spanId);
        span.hidden = false;
        span.innerHTML = message.innerHTML;
        const input = span.closest('.form-element-container').querySelector('input, select');
        input.classList.add('error');
      }
    }
});
