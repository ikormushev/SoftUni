function attachEventsListeners() {
    let conversions = {
        'km': {
            "m": (x) => x * 1000,
        },
        "m": {
            "km": (x) => x / 1000,
            "m": (x) => x,
            "cm": (x) => x * 100,
            "mm": (x) => x * 100 * 10,
            "mi": (x) => x * 0.000621371192,
            "yrd": (x) => x * 1.0936133,
            "ft": (x) => x * 3.2808399,
            "in": (x) => x * 39.3700787,
        },
        "cm": {
            "m": (x) => x * 0.01,
        },
        "mm": {
            "m": (x) => x * 0.001,
        },
        "mi": {
            "m": (x) => x * 1609.34,
        },
        "yrd": {
            "m": (x) => x * 0.9144,
        },
        "ft": {
            "m": (x) => x * 0.3048,
        },
        "in": {
            "m": (x) => x * 0.0254,
        }
    }

    let convertButton = document.getElementById('convert');
    convertButton.addEventListener('click', () => {
        let inputEl = document.getElementById('inputDistance');
        let inputElValue = Number(inputEl.value);
        let inputSelectValue = document.getElementById('inputUnits').value;
    
        let outputEl = document.getElementById('outputDistance');
        let outputSelectValue = document.getElementById('outputUnits').value;

        let resultInM = conversions[inputSelectValue]["m"](inputElValue);
        let result = conversions["m"][outputSelectValue](resultInM);
        outputEl.value = result;
    });

}
