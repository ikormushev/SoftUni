function loadCommits() {
    let inputUsername = document.getElementById('username').value;
    let inputRepo = document.getElementById('repo').value;
    let commitsUl = document.getElementById('commits');

    async function getCommits() {
        try {
            const response = await fetch(`https://api.github.com/repos/${inputUsername}/${inputRepo}/commits`);
            if (!response.ok) {
                throw new Error(response.status);
            }

            let data = await response.json();
            data.forEach(currCommit => {
                let newLi = document.createElement('li');

                let authorName = currCommit.commit.author.name;
                let message = currCommit.commit.message;
                newLi.textContent = (`${authorName}: ${message}`);
                commitsUl.appendChild(newLi);
            });

        } catch(error) {
            let newLi = document.createElement('li');
            newLi.textContent = `Error: ${error.message} (Not Found)`;
            commitsUl.appendChild(newLi);
        }
    }

    getCommits();
}
