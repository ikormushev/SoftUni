const mainUrl = "http://localhost:3030/jsonstore/matches";

const loadMatchesButton = document.getElementById('load-matches');
const matchesUl = document.getElementById('list');
const addMatchButton = document.getElementById('add-match');
const editMatchButton = document.getElementById('edit-match');

const hostEl = document.getElementById('host');
const scoreEl = document.getElementById('score');
const guestEl = document.getElementById('guest');

const formEl = document.querySelector('#form form');

loadMatchesButton.addEventListener('click', async () => {
    let response = await fetch(mainUrl);
    let data = await response.json();
    let matchesData = Object.values(data);

    matchesUl.innerHTML = "";
    matchesData.forEach(match => addMatch(match.host, match.score, match.guest, match._id));
});

function addMatch(matchHost, matchScore, matchGuest, matchId) {
    let newLi = document.createElement('li');
    newLi.classList.add('match');

    let infoDiv = document.createElement('div');
    infoDiv.classList.add('info');

    let hostP = document.createElement('p');
    hostP.textContent = matchHost;
    let scoreP = document.createElement('p');
    scoreP.textContent = matchScore;
    let guestP = document.createElement('p');
    guestP.textContent = matchGuest;

    infoDiv.appendChild(hostP);
    infoDiv.appendChild(scoreP);
    infoDiv.appendChild(guestP);

    let buttonDiv = document.createElement('div');
    buttonDiv.classList.add('btn-wrapper');

    let changeButton = document.createElement('button');
    changeButton.classList.add('change-btn');
    changeButton.textContent = "Change";
    changeButton.addEventListener('click', () => {
        hostEl.value = matchHost;
        scoreEl.value = matchScore;
        guestEl.value = matchGuest;

        editMatchButton.disabled = false;
        addMatchButton.disabled = true;

        formEl.setAttribute('match-id', matchId);
    });

    let deleteButton = document.createElement('button');
    deleteButton.classList.add('delete-btn');
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener('click', async () => {
        let response = await fetch(`${mainUrl}/${matchId}`, {
            method: 'DELETE',
        });

        loadMatchesButton.click();
    });

    buttonDiv.appendChild(changeButton);
    buttonDiv.appendChild(deleteButton);

    newLi.appendChild(infoDiv);
    newLi.appendChild(buttonDiv);

    matchesUl.appendChild(newLi);
}

addMatchButton.addEventListener('click', async () => {
    let response = await fetch(mainUrl, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({host: hostEl.value, score: scoreEl.value, guest: guestEl.value})
    });

    if (response.ok === true) {
        loadMatchesButton.click();
    }

    hostEl.value = "";
    scoreEl.value = "";
    guestEl.value = "";
});

editMatchButton.addEventListener('click', async () => {
    let editMatchId = formEl.getAttribute('match-id');
    let newHost = hostEl.value;
    let newScore = scoreEl.value;
    let newGuest = guestEl.value;

    let response = await fetch(`${mainUrl}/${editMatchId}`, {
        method: "PUT",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({host: newHost, score: newScore, guest: newGuest}),
    })

    loadMatchesButton.click();
    editMatchButton.disabled = true;
    addMatchButton.disabled = false;
    formEl.removeAttribute('match-id');
});

