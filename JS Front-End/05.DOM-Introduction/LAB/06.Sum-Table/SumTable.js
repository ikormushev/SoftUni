function sumTable() {
    let pricesElements = document.querySelectorAll("tr td:nth-child(even):not(#sum)");
    let totalSum = 0;
    pricesElements.forEach(x => totalSum += Number(x.textContent));

    let lastPriceElement = document.querySelector("tr #sum");
    lastPriceElement.textContent = totalSum;
}
