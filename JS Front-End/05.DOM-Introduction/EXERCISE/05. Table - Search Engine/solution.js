function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let searchText = document.getElementById('searchField');
      let searchTextValue = searchText.value;
      let table = document.querySelectorAll('.container tbody tr');

      for (let col of table) {
         let splitText = col.innerText.toLowerCase();

         if (splitText.includes(searchTextValue.toLowerCase())) {
            col.classList.add('select');
         } else {
            col.classList.remove('select');
         }
      }

      searchText.value = '';
   }
}
