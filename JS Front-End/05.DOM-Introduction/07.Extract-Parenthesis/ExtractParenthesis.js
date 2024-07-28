function extract(content) {
    let wantedElement = document.getElementById(content);

    let matchesFound = wantedElement.textContent.match(/(?<=\()[a-zA-Z ]+(?=\))/g) || [];
    return matchesFound.join("; ");
}
