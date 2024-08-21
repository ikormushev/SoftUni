window.addEventListener("load", solve);

function solve() {
    let addButton = document.getElementById('add-btn');
    let eventNameEl = document.getElementById('name');
    let dateOrTimeEl = document.getElementById('time');
    let descriptionTextarea = document.getElementById('description');

    let eventUl = document.getElementById('preview-list');
    let archiveUl = document.getElementById('archive-list');

    addButton.addEventListener('click', () => {
        createTaskEvent(eventNameEl.value, dateOrTimeEl.value, descriptionTextarea.value);
    });

    function createTaskEvent(eventName, eventTime, eventDescription) {
        let newLi = document.createElement('li');

        let articleEl = document.createElement('article');

        let titleP = document.createElement('p');
        titleP.textContent = eventName;

        let timeP = document.createElement('p');
        timeP.textContent = eventTime;

        let descriptionP = document.createElement('p');
        descriptionP.textContent = eventDescription;

        articleEl.appendChild(titleP);
        articleEl.appendChild(timeP);
        articleEl.appendChild(descriptionP);

        let buttonsDiv = document.createElement('div');
        buttonsDiv.classList.add('buttons');

        let editButton = document.createElement('button');
        editButton.classList.add('edit-btn');
        editButton.textContent = "Edit";
        editButton.addEventListener('click', () => {
            eventNameEl.value = eventName;
            dateOrTimeEl.value = eventTime;
            descriptionTextarea.value = eventDescription;

            newLi.remove();
            addButton.disabled = false;
        });

        let nextButton = document.createElement('button');
        nextButton.classList.add('next-btn');
        nextButton.textContent = "Next";
        nextButton.addEventListener('click', () => {

            let archiveButton = document.createElement('button');
            archiveButton.classList.add('archive-btn');
            archiveButton.textContent = "Archive";
            archiveButton.addEventListener('click', () => {
                newLi.remove();
                addButton.disabled = false;
            });
            newLi.appendChild(archiveButton);
            archiveUl.appendChild(newLi);
            buttonsDiv.remove();
        });

        buttonsDiv.appendChild(editButton);
        buttonsDiv.appendChild(nextButton);

        newLi.appendChild(articleEl);
        newLi.appendChild(buttonsDiv);

        eventUl.appendChild(newLi);

        eventNameEl.value = "";
        dateOrTimeEl.value = "";
        descriptionTextarea.value = "";
        addButton.disabled = true;
    }
}