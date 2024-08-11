function loadRepos() {
	let input = document.querySelector('input[type="text"]').value;
	let reposList = document.getElementById('repos');

	async function allRepos() {
		try {
			let response = await fetch(`https://api.github.com/users/${input}/repos`);
			if (!response.ok) {
				throw new Error(`${response.status} ${response.statusText}`);
			}

			let data = await response.json();
			data.forEach(repo => {
				const listItem = document.createElement("li");
				const link = document.createElement("a");
				link.href = repo.html_url;
				link.textContent = repo.full_name;

				listItem.appendChild(link);
				reposList.appendChild(listItem);
			});

		} catch(error) {
			const listItem = document.createElement("li");
			listItem.textContent = `Error: ${error.message}`;
			reposList.appendChild(listItem);
		}
	}

	allRepos();

}
