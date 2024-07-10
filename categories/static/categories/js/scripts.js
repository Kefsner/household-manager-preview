// ===== Create Subcategory Modal =====
function openCreateSubcategoryModal(categoryId, categoryName) {
    const category = document.getElementById('subcategory-category-name');
    category.innerHTML = categoryName;
    const Form = document.getElementById('create-subcategory-form');
    Form.action = '/categories/' + categoryId + '/create_subcategory/';
    toggleModal('create-subcategory-modal');
}

// ===== Toggle Subcategories table =====
function toggleSubcategories(categoryId) {
    const subcategories = document.getElementById(categoryId);
    subcategories.classList.toggle('show');
}

// ===== Expand All Subcategories tables =====
function expandAllSubcategories() {
  console.log('expandAllSubcategories');
    const subcategories = document.querySelectorAll('.subcategory-table');
    subcategories.forEach((subcategory) => {
        subcategory.classList.add('show');
    });
}

// ===== Collapse All Subcategories tables =====
function collapseAllSubcategories() {
  console.log('collapseAllSubcategories');
    const subcategories = document.querySelectorAll('.subcategory-table');
    subcategories.forEach((subcategory) => {
        subcategory.classList.remove('show');
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