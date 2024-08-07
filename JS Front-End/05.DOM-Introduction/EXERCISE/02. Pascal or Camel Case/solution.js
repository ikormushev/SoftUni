function solve() {
  let resultElement = document.getElementById('result');
  let casing = document.getElementById('naming-convention').value;
  let text = document.getElementById('text').value;

  let output = '';
  let currText = text.split(" ");
  let newText = currText.map(x => x.toLowerCase());

  if (casing === 'Pascal Case') {
    output = newText.map(x => x.charAt(0).toUpperCase() + x.slice(1)).join("");
  } else if (casing === 'Camel Case') {
    output = newText.shift() + newText.map(x => x.charAt(0).toUpperCase() + x.slice(1)).join("");
  }  else {
      output = 'Error!';
  }

  resultElement.textContent = output;
}
