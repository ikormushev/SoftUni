function calc() {
    let num1Element = document.getElementById("num1");
    let num2Element = document.getElementById("num2");
    let sumElement = document.getElementById("sum");

    let num1Value = Number(num1Element.value);
    let num2Value = Number(num2Element.value);

    sumElement.value = num1Value + num2Value;
}
