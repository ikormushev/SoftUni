function loadRepos() {
   let loadButton = document.querySelector('button');

   loadButton.addEventListener('click', () => {
      async function loadRepo() {
         let response = await fetch('https://api.github.com/users/testnakov/repos');
            let repoData = await response.text();
   
            let divEL = document.getElementById('res');
            divEL.textContent = repoData;
      }

      loadRepo();
   });
}
