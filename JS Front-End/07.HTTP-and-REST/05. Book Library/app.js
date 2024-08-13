const booksURL = 'http://localhost:3030/jsonstore/collections/books';
const loadBooksButton = document.getElementById('loadBooks');
const submitBookButton = document.querySelector('#form button');


loadBooksButton.addEventListener('click', () => {
    let tableBody = document.querySelector('table tbody');
    let tableRows = tableBody.querySelectorAll('tr');
    tableRows.forEach(x => x.remove());

    async function getBooks() {
        try {
            const response = await fetch(booksURL);

            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            
            let data = await response.json();
            let dataBooks = Object.entries(data);
        
            dataBooks.forEach(bookObject => {
                let book = bookObject[1];
                let newRow = document.createElement('tr');

                let titleCol = document.createElement('td');
                titleCol.textContent = book.title;

                let authorCol = document.createElement('td');
                authorCol.textContent = book.author;

                let buttonsCol = document.createElement('td');
                let editButton = document.createElement('button');
                editButton.textContent = "Edit";
                editButton.addEventListener('click', () => {
                    async function editBook(updateFields) {
                        try {
                            const response = await fetch(`${booksURL}/${bookObject[0]}`, {
                                method: "PUT",
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify(updateFields)
                            });

                            if (!response.ok) {
                                throw new Error(`Error: ${response.status}`);
                            }

                            console.log(`Successfully edited Book to ${updateFields.title} ${updateFields.author}`)
                            loadBooksButton.click();
                        } catch(error) {
                            console.log(error.message);
                        }
                    }

                    let newTitle = document.querySelector('#form input[type="text"][name="title"]').value;
                    let newAuthor = document.querySelector('#form input[type="text"][name="author"]').value;
                
                    editBook({title: newTitle, author: newAuthor});
                });
    
                let deleteButton = document.createElement('button');
                deleteButton.textContent = "Delete";
                deleteButton.addEventListener('click', () => {
                    async function deleteBook() {
                        try {
                            const response = await fetch(`${booksURL}/${bookObject[0]}`, {
                                method: "DELETE"
                            });

                            if (!response.ok) {
                                throw new Error(`Error: ${response.status}`);
                            }

                            loadBooksButton.click();
                        } catch(error) {
                            console.log(error.message);
                        }
                    }

                    deleteBook();
                });
                
                buttonsCol.appendChild(editButton);
                buttonsCol.appendChild(deleteButton);

                // Add all to the new row
                newRow.appendChild(titleCol);
                newRow.appendChild(authorCol);
                newRow.appendChild(buttonsCol);

                // Add the new row to the table
                tableBody.appendChild(newRow);
            });

        } catch (error){
            console.log(error.message);
        }
    }

    getBooks();
});

submitBookButton.addEventListener('click', () => {
    let titleNameEl = document.querySelector('#form input[type="text"][name="title"]');
    let titleName = titleNameEl.value;

    let authorNameEl = document.querySelector('#form input[type="text"][name="author"]');
    let authorName = authorNameEl.value;

    async function createBook() {
        try {
            const response = await fetch(booksURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({title: titleName, author: authorName})
            });

            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }

            let responseReturn = await response.json();
            console.log(`Successfully added Book with Title ${responseReturn.title} and ${responseReturn.author}`);
            loadBooksButton.click();

        } catch (error) {
            console.log(error.message);
        }
    }

    createBook();
});
