function create(words) {
   let contentDiv = document.getElementById('content');

   for (let paragraphName of words) {
      let newDiv = document.createElement('div');
      let newParagraph = document.createElement('p');
      newParagraph.textContent = paragraphName;
      newParagraph.style.display = 'none';
      newDiv.appendChild(newParagraph);

      newDiv.addEventListener('click', () => {
         let paragraphInside = newDiv.querySelector('p');
         paragraphInside.style.display = 'block';
      });
      contentDiv.appendChild(newDiv);
   }
}
