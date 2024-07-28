function editElement(givenElement, match, replacement) {
    givenElement.textContent = givenElement.textContent.replaceAll(match, replacement);
}
