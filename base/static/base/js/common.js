// Enhanced delete URL to prevent accidental deletion
const DELETE_URL = "delete-4f3d2a1b-1b3c-4a2b-8c1a-3b2c1a4f3d2a";

// Reset form, remove error classes, and hide error spans
function resetForm(form) {
    form.reset();
    const fields = form.querySelectorAll("input, select");
    fields.forEach((input) => {
        input.classList.remove("error");
    });
    const spans = form.querySelectorAll("span");
    spans.forEach((span) => {
        span.hidden = true;
        span.innerHTML = "";
    });
    const urlInput = form.querySelector('input[name="url"]');
    if (urlInput) {
        form.removeChild(urlInput);
    };
}

// Necessary for redirecting to the current page after form submission
function addUrlToForm(form) {
    const currentUrl = window.location.href;
    const urlInput = document.createElement("input");
    urlInput.type = "hidden";
    urlInput.name = "url";
    urlInput.value = currentUrl;
    form.appendChild(urlInput);
}

// Toggle modal visibility
function toggleModal(modalId) {
    const modal = document.querySelector(`#${modalId}`);
    const form = modal.querySelector("form");
    if (modal.classList.contains("show")) {
        resetForm(form);
    } else {
        addUrlToForm(form);
    }
    modal.classList.toggle("show");
}

// Open delete modal with item name and form action
function openDeleteModal(type, itemId, itemName) {
    const item = document.querySelector(`#${type}-name`);
    item.innerHTML = itemName;
    const form = document.querySelector(`#delete-${type}-form`);
    form.action = get_delete_url(type, itemId);
    toggleModal(`delete-${type}-modal`);
}

// Get delete URL for item
function get_delete_url(type, itemId) {
    if  (type === "subcategory") {
        return `/${pluralize("category")}/${DELETE_URL}/subcategory/${itemId}/`;
    } else {
        return `/${pluralize(type)}/${DELETE_URL}/${itemId}/`;
    }
}

// Pluralize type for matching view URLs
function pluralize(type) {
    const irregularPlurals = {
        "category": "categories",
        "subcategory": "subcategories"
    };
    return irregularPlurals[type] || `${type}s`;
}
