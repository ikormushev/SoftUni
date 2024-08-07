function addItem() {
    let listOfItems = document.getElementById('items');
    let itemText = document.getElementById('newItemText').value;

    let newItem = document.createElement('li');
    newItem.textContent = itemText;

    let newLink = document.createElement('a');
    newLink.textContent = "[Delete]";
    newLink.href = "#";
    newLink.addEventListener('click', () => newItem.remove());
    newItem.appendChild(newLink);

    listOfItems.appendChild(newItem);
}
