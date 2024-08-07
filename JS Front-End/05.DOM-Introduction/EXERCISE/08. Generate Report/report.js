function generateReport() {
    let headElementInputs = document.querySelectorAll('table thead tr th');
    let table = document.querySelectorAll('table tbody tr');
    let outputEl = document.getElementById('output');

    let resultArr = [];

    for (let row of table) {
        let rowElements = row.querySelectorAll('td');
        let rowObj = {};

        for (let i = 0; i < rowElements.length; i++) {
            let isChecked = headElementInputs[i].querySelector('input').checked;
            
            if (isChecked) {
                let keyName = headElementInputs[i].textContent.toLowerCase().trim();
                rowObj[keyName] = rowElements[i].textContent;
            }
        }
        resultArr.push(rowObj);
    }

    let result = JSON.stringify(resultArr, null, 2);
    outputEl.value = result;
}
