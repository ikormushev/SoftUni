function toggle() {
    let buttonElement = document.getElementsByClassName('button')[0];
    let textElement = document.getElementById('extra');

    if (buttonElement.textContent === 'Less') {
        buttonElement.textContent = 'More';
        textElement.style.display = 'none';
    } else if (buttonElement.textContent === 'More') {
        buttonElement.textContent = 'Less';
        textElement.style.display = 'block';
    }
}
