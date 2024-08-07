function search() {
   let townsList = document.querySelectorAll('#towns li');
   let totalTownsFound = 0;

   let textSearch = document.getElementById('searchText').value;
   let resultDiv = document.getElementById('result');

   for (let town of townsList) {
      let townContent = town.textContent;

      if (townContent.includes(textSearch)) {
         totalTownsFound++;
         town.style.fontWeight = 'bold';
         town.style.textDecoration = 'underline';
      } else {
         town.style.fontWeight = 'none';
         town.style.textDecoration = 'none';
      }
   }
   resultDiv.textContent = `${totalTownsFound} matches found`;
}
