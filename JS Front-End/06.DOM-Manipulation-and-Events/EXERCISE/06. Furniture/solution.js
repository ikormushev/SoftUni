function solve() {
    let [generateButton, buyButton] = document.querySelectorAll('#exercise button');

    generateButton.addEventListener('click', () => {
        let inputTextArea = document.querySelector('#exercise textarea');
        let jsonInput = JSON.parse(inputTextArea.value);
        console.log(jsonInput);

        for (let furnitureObject of jsonInput) {
            let furnitureTableBody = document.querySelector('tbody');

            let newRow = document.createElement('tr');

            let imageCol = document.createElement('td');
            let imageEl = document.createElement('img');
            imageEl.src = furnitureObject['img'];
            imageCol.appendChild(imageEl);

            let nameCol = document.createElement('td');
            let nameP = document.createElement('p');
            nameP.textContent = furnitureObject["name"];
            nameCol.appendChild(nameP);

            let priceCol = document.createElement('td');
            let priceP = document.createElement('p');
            priceP.textContent = furnitureObject["price"];
            priceCol.appendChild(priceP);

            let decorationCol = document.createElement('td');
            let decorationP = document.createElement('p');
            decorationP.textContent = furnitureObject["decFactor"];
            decorationCol.appendChild(decorationP);

            let markCol = document.createElement('td');
            let markInput = document.createElement('input');
            markInput.type = "checkbox";
            markCol.appendChild(markInput);

            // Add every column to the row
            newRow.appendChild(imageCol);
            newRow.appendChild(nameCol);
            newRow.appendChild(priceCol);
            newRow.appendChild(decorationCol);
            newRow.appendChild(markCol);
            furnitureTableBody.appendChild(newRow);
        }
    });

    buyButton.addEventListener('click', () => {
        let resultTextBox = document.querySelectorAll('#exercise textarea')[1];

        let totalPrice = 0;
        let averageDecFactor = 0;
        let productsBought = [];

        let products = document.querySelectorAll('.table tbody tr');

        for (let productRow of products) {
            let [image, nameCol, priceCol, decFactorCol, markCol] = productRow.querySelectorAll('td');

            let name = nameCol.querySelector('p').textContent;
            let price = Number(priceCol.querySelector('p').textContent);
            let decFactor = Number(decFactorCol.querySelector('p').textContent);
            let mark = markCol.querySelector('input').checked;

            if (mark === true) {
                productsBought.push(name);
                totalPrice += price;
                averageDecFactor += decFactor;
            }
        }

        resultTextBox.value += `Bought furniture: ${productsBought.join(", ")}\n`;
        resultTextBox.value += `Total price: ${totalPrice.toFixed(2)}\n`;
        resultTextBox.value += `Average decoration factor: ${averageDecFactor / productsBought.length}`;
    });
}
