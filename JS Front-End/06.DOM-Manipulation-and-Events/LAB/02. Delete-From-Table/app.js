function deleteByEmail() {
    let emailInput = document.querySelector('label input');
    let table = document.querySelectorAll('tbody tr');
    let resultEl = document.getElementById('result');
    let isDeleted = false;

    for (let row of table) {
        let rowContent = row.querySelectorAll('td');
        
        for (let col of rowContent) {
            if (col.textContent.includes(emailInput.value)) {
                row.remove();
                isDeleted = true;
            }
        }
    }
    if (isDeleted) {
        resultEl.textContent = "Deleted.";
    } else {
        resultEl.textContent = "Not found.";
    }
}
