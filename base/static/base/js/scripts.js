function toggleCircleButton() {
  const circleButton = document.querySelector("#circle-button");
  const content = document.querySelector("#circle-button-content");
  const isActive = circleButton.classList.contains("active");
  circleButton.innerHTML = isActive ? "+" : "-";
  circleButton.classList.toggle("active");
  content.classList.toggle("show");
}

function openTransactionModal(type) {
  toggleCircleButton();
  toggleModal(`${type}-modal`);
}

// Setup Event Listeners
document.addEventListener("DOMContentLoaded", function () {
  autoUpdateSubcategories();
  autoUpdateToAccount();
  handleFormErrors();
});

// DOMContentLoaded Event Listener method
function autoUpdateSubcategories() {
  const categories = document.querySelectorAll(".category-dropdown");
  const subcategories = document.querySelectorAll(".subcategory-dropdown");

  // Hide all subcategories
  subcategories.forEach((subcategory) => {
    Array.from(subcategory.options).forEach((option) => {
      option.hidden = true;
    });
  });

  // Add event listener to each category dropdown
  categories.forEach((category, index) => {
    category.addEventListener("change", function () {
      const selectedCategoryId = category.value;
      const subcategory = subcategories[index];
      const options = Array.from(subcategory.options);
      options.forEach((option) => {
        option.hidden = !option.classList.contains(
          `category-${selectedCategoryId}`
        );
      });
      // Reset the selected subcategory
      subcategory.value = "";
    });
  });
}

// DOMContentLoaded Event Listener method
function autoUpdateToAccount() {
  const accounts = document.querySelectorAll("#transfer-account");
  const toAccounts = document.querySelectorAll("#transfer-to_account");

  // Hide all to_accounts
  toAccounts.forEach((toAccount) => {
    Array.from(toAccount.options).forEach((option) => {
      option.hidden = true;
    });
  });

  // Add event listener to each account dropdown
  accounts.forEach((account, index) => {
    account.addEventListener("change", function () {
      const selectedAccountId = account.value;
      const toAccount = toAccounts[index];
      const toAccountOptions = Array.from(toAccount.options);
      toAccountOptions.forEach((option) => {
        option.hidden = option.value === selectedAccountId || option.value === "";
      });
      // Reset the selected to_account
      toAccount.value = "";
    });
  });
}

//DOMContentLoaded Event Listener method
function handleFormErrors() {
  const message = document.querySelector(".message-content");
  const tags = document.querySelector(".message-tags");
  if (message && tags) {
    const [formType, field] = tags.innerHTML.split(" ");
    if (formType === "page") {
      handlePageSpecificFormErrors(field, message);
      return;
    }
    const span = document.querySelector(`#${formType}-${field}-error`);
    span.hidden = false;
    span.innerHTML = message.innerHTML;
    const input = span
      .closest(".form-element-container")
      .querySelector("input, select");
    input.classList.add("error");
    toggleModal(`${formType}-modal`);
  }
}
