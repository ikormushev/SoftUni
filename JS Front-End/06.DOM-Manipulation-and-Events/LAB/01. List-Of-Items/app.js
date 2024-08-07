function addItem() {
    let listOfItems = document.getElementById('items');
    let itemText = document.getElementById('newItemText').value;

    let newItem = document.createElement('li');
    newItem.textContent = itemText;
    listOfItems.appendChild(newItem);
}
