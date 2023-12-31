document.addEventListener('DOMContentLoaded', function() {
  var addButton = document.getElementById('add-field');
  var removeButton = document.getElementById('remove-field');
  var availableFields = document.getElementById('available-fields');
  var selectedFields = document.getElementById('selected-fields');
  var nextButton = document.querySelector('.next-button');

  // Array to store selected fields
  var selectedFieldsArray = [];

  addButton.addEventListener('click', function() {
    moveSelectedOptions(availableFields, selectedFields);

    // Update the array with the current selected fields
    selectedFieldsArray = getSelectedFieldsArray();
  });

  removeButton.addEventListener('click', function() {
    moveSelectedOptions(selectedFields, availableFields);

    // Update the array with the current selected fields
    selectedFieldsArray = getSelectedFieldsArray();
  });

  // Function to move selected options between select elements
  function moveSelectedOptions(fromSelect, toSelect) {
    Array.from(fromSelect.selectedOptions).forEach(function(option) {
      toSelect.appendChild(option);
    });
  }

  // Function to get an array of selected fields
  function getSelectedFieldsArray() {
    return Array.from(selectedFields.options).map(function(option) {
      return option.value;
    });
  }

  nextButton.addEventListener('click', function() {
    var queryString = '?selectedFields=' + encodeURIComponent(JSON.stringify(selectedFieldsArray));
    window.location.href = '/task-1' + queryString;
  });
});
