function lockedProfile() {
    let profiles = document.querySelectorAll('.profile');

    for(let profile of profiles) {
        let infoDiv = profile.querySelector('div');
        let showMoreButton = profile.querySelector('button');

        showMoreButton.addEventListener('click', () => {
            let radioButtons = profile.querySelectorAll('input[type="radio"]');
            let lockValue = radioButtons[0].checked;
            if (lockValue === false) {
                if (showMoreButton.textContent === "Hide it") {
                    infoDiv.style.display = 'none';
                    showMoreButton.textContent = "Show more";
                } else {
                    infoDiv.style.display = 'block';
                    showMoreButton.textContent = "Hide it";
                }
            } 
        });
    }
}
