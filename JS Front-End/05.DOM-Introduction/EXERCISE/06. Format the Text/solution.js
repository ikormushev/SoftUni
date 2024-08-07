function solve() {
  let givenTextEl = document.getElementById('input');
  let sentences = givenTextEl.value.split('.')
                  .map(x => x.trim())
                  .filter(x => x.length > 0);

  let outputEl = document.getElementById('output');
  outputEl.innerHTML = '';

  for (let i = 0; i < sentences.length; i += 3) {
    let newSentence = sentences.slice(i, i + 3).join('. ') + '.';
    outputEl.innerHTML += `<p>${newSentence}</p>`;
  }
}
