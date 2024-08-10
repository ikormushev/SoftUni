function addItem() {
    let selectOptions = document.getElementById('menu');
    let textEl = document.getElementById('newItemText');
    let valueEl = document.getElementById('newItemValue');

    let newOption = document.createElement('option');
    newOption.textContent = textEl.value;
    newOption.value = valueEl.value;
    selectOptions.appendChild(newOption);

    textEl.value = "";
    valueEl.value = "";
}
