function encodeAndDecodeMessages() {
    let [encodeFieldButton, decodeFieldButton] = document.querySelectorAll('#container #main div button');

    encodeFieldButton.addEventListener('click', () => {
        let [currEncodeField, currDecodeField] = document.querySelectorAll('#container #main div');

        let currEncodeTextarea = currEncodeField.querySelector('textarea');
        let currDecodeTextarea = currDecodeField.querySelector('textarea');
        
        let newString = "";

        for (let currChar of currEncodeTextarea.value) {
            let asciiValue = currChar.charCodeAt(0);
            asciiValue++;
            newString += String.fromCharCode(asciiValue);
        }
        currEncodeTextarea.value = "";
        currDecodeTextarea.value = newString;
    });

    decodeFieldButton.addEventListener('click', () => {
        let [currEncodeField, currDecodeField] = document.querySelectorAll('#container #main div');

        let currEncodeTextarea = currEncodeField.querySelector('textarea');
        let currDecodeTextarea = currDecodeField.querySelector('textarea');
        
        let newString = "";

        for (let currChar of currDecodeTextarea.value) {
            let asciiValue = currChar.charCodeAt(0);
            asciiValue--;
            newString += String.fromCharCode(asciiValue);
        }
        currDecodeTextarea.value = newString;
    });
}
