function subtract() {
    let firstNumberElementValue = Number(document.getElementById('firstNumber').value);
    let secondNumberElementValue = Number(document.getElementById('secondNumber').value);

    let resultValue = firstNumberElementValue - secondNumberElementValue;
    let newElement = document.createTextNode(resultValue);

    let resultDiv = document.getElementById('result');
    resultDiv.appendChild(newElement);
}
