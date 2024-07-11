// ===== Create Subcategory Modal =====
function openCreateSubcategoryModal(categoryId, categoryName) {
    const category = document.getElementById('subcategory-category-name');
    category.innerHTML = categoryName;
    const Form = document.getElementById('create-subcategory-form');
    Form.action = '/categories/' + categoryId + '/create_subcategory/';
    toggleModal('create-subcategory-modal');
}

// ===== Toggle Subcategories table =====
function toggleSubcategories(subcategoryTableId) {
    const subcategories = document.getElementById(subcategoryTableId);
    subcategories.classList.toggle('show');
    updateEyeIcon(subcategoryTableId.split('-')[2]);
}

function updateEyeIcon(categoryId) {
  const eyeIcon = document.getElementById(`show-subcategories-icon-${categoryId}`)
  const subcategories = document.getElementById(`subcategory-table-${categoryId}`);
  if (subcategories.classList.contains('show')) {
    eyeIcon.src = '/static/base/icon/eye-slash.svg';
  } else {
    eyeIcon.src = '/static/base/icon/eye.svg';
  }
}

// ===== Expand All Subcategories tables =====
function expandAllSubcategories() {
    const subcategories = document.querySelectorAll('.subcategory-table');
    subcategories.forEach((subcategory) => {
        subcategory.classList.add('show');
        categoryId = subcategory.id.split('-')[2];
        updateEyeIcon(categoryId);
    });
}

// ===== Collapse All Subcategories tables =====
function collapseAllSubcategories() {
    const subcategories = document.querySelectorAll('.subcategory-table');
    subcategories.forEach((subcategory) => {
        subcategory.classList.remove('show');
        categoryId = subcategory.id.split('-')[2];
        updateEyeIcon(categoryId);
    });
}

// ===== Handle Page Specific Form Errors =====
function handlePageSpecificFormErrors(field, message) {
    let spanId;
    let pk;
    let id;
    let categoryName;
    if (field.endsWith('_subcategory')) {
      field = field.replace('_subcategory', '');
      [field, pk] = field.split('_');
      [id, categoryName] = pk.split('-');
      spanId = `create-subcategory-${field}-error`;
      openCreateSubcategoryModal(id, categoryName);
    } else {
      spanId = `create-category-${field}-error`;
      toggleModal('create-category-modal');
    }
    const span = document.getElementById(spanId);
    span.hidden = false;
    span.innerHTML = message.innerHTML;
    const input = span.closest('.form-element-container').querySelector('input, select');
    input.classList.add('error');
}