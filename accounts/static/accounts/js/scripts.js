const DELETE_URL = 'delete-4f3d2a1b-1b3c-4a2b-8c1a-3b2c1a4f3d2a';

const deleteModal = document.querySelector('.modal-container.delete');

function toggleDeleteModal() {
  deleteModal.classList.toggle('show');
}

function openDeleteModal(itemId, itemName) {
    const itemToDelete = document.getElementById('item-name');
    itemToDelete.innerHTML = itemName;
    const deleteForm = document.getElementById('delete-form');
    deleteForm.action = '/accounts/' + DELETE_URL + "/" + itemId + "/";
    toggleDeleteModal();
}