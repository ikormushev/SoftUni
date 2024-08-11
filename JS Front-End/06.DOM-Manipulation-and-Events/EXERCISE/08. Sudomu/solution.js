function solve() {
    let [buttonCheck, buttonClear] = document.querySelectorAll('tfoot button');
    let table = document.querySelector('#exercise table');

    buttonCheck.addEventListener('click', () => {
        let table = document.querySelector('#exercise table');
        let sudokuMatrix = [];
        let tableRows = table.querySelectorAll('tbody tr');

        for (let row of tableRows) {
            let rowCols = row.querySelectorAll('td input');
            let newRow = [];

            for (let col of rowCols) {
                newRow.push(Number(col.value));
            }

            sudokuMatrix.push(newRow);
        }

        let isInvalid = false;
    
        for (let i = 0; i < sudokuMatrix.length; i++) {
            let rowSet = new Set();
            let colSet = new Set();
        
            for (let j = 0; j < sudokuMatrix.length; j++) {
                let rowEl = sudokuMatrix[i][j];
                let colEl = sudokuMatrix[j][i];
        
                if (rowSet.has(rowEl)) {
                    isInvalid = true;
                    break;
                }
                rowSet.add(rowEl);

                if (colSet.has(colEl)) {
                    isInvalid = true;
                    break;
                }
                colSet.add(colEl);
            }
        
            if (isInvalid) {
                break;
            }
        }

        let checkDivP = document.querySelector('#check p');

        if (isInvalid) {
            table.style.border = "2px solid red";
            checkDivP.textContent = 'NOP! You are not done yet...';
            checkDivP.style.color = "red";
        } else {
            table.style.border = "2px solid green";
            checkDivP.textContent = 'You solve it! Congratulations!';
            checkDivP.style.color = "green";
        }
    });
    buttonClear.addEventListener('click', () => {
        let table = document.querySelector('#exercise table');
        table.style.border = "none";
        let checkDivP = document.querySelector('#check p');
        checkDivP.textContent = "";
        let tableRowsValues = table.querySelectorAll('tbody tr td input');
        tableRowsValues.forEach(x => x.value = "");
    });

}
