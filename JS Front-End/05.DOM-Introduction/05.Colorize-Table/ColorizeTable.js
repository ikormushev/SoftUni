function colorize() {
    let wantedElements = document.querySelectorAll("table tr:nth-child(even)");
    wantedElements.forEach(x => x.style.backgroundColor = "teal");
}
