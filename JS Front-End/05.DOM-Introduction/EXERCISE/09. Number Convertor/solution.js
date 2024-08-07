function solve() {
    document.querySelector("button").addEventListener('click', onClick);

    let selectMenu = document.getElementById('selectMenuTo');

    let binaryOption = document.createElement('option');
    binaryOption.value = 'binary';
    binaryOption.textContent = 'Binary';

    const hexOption = document.createElement('option');
    hexOption.value = 'hexadecimal';
    hexOption.textContent = 'Hexadecimal';

    selectMenu.appendChild(binaryOption);
    selectMenu.appendChild(hexOption);

    let conversionObj = {
        'binary': x => x.toString(2),
        'hexadecimal': x => x.toString(16).toUpperCase()
    }

    function onClick() {
        let inputValue = Number(document.getElementById('input').value);
        let output = document.getElementById('result');
        let selectValue = selectMenu.value;

        let result = conversionObj[selectValue](inputValue);
        output.value = result;
    }
}
