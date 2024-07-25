// Task 1
function carWash(arr) {
    let start = 0;

    let actions = {
        soap: x => x + 10,
        water: x => x * 1.20,
        "vacuum cleaner": x => x * 1.25,
        mud: x => x * 0.90
    };

    for (action of arr) {
        start = actions[action](start);
    }

    console.log(`The car is ${start.toFixed(2)}% clean.`);
}

// Task 2
function numberModification(num) {
    let currNum = String(num);
    let numAverage = currNum
                    .split('')
                    .map(x => Number(x))
                    .reduce((x, y) => x + y) 
                        / currNum.length;

    while (numAverage <= 5) {
        currNum += 9;

        numAverage = currNum
                    .split('')
                    .map(x => Number(x))
                    .reduce((x, y) => x + y) 
                        / currNum.length;
    }

    console.log(currNum);
}

// Task 3
function pointsValidation(points) {
    let [x1, y1, x2, y2] = points;
    let validPoints = [];

    function calculate(newX1, newY1, newX2, newY2) {
        let formulaResult = Math.sqrt((newX2 - newX1) ** 2 + (newY2 - newY1) ** 2);
        if (Number.isInteger(formulaResult)) {
            return `{${newX1}, ${newY1}} to {${newX2}, ${newY2}} is valid`
        }
    
        return `{${newX1}, ${newY1}} to {${newX2}, ${newY2}} is invalid`
    }

    validPoints.push(calculate(x1, y1, 0, 0));
    validPoints.push(calculate(x2, y2, 0, 0));
    validPoints.push(calculate(x1, y1, x2, y2));

    console.log(validPoints.join("\n"));
}

// Task 4
function radioCrystals(arr) {
    let [target, ...chunks] = arr;

    let operations = {
        'Cut': {func: x => x / 4, count: 0},
        'Lap': {func: x => x * 0.80, count: 0},
        'Grind': {func: x => x - 20, count: 0},
        'Etch': {func: x => x - 2, count: 0},
    };

    let transportingAndWashing = x => Math.floor(x);
    let xRay = x => x + 1;

    for (let chunk of chunks) {
        console.log(`Processing chunk ${chunk} microns`);
        for (let operation in operations) {
            while (operations[operation].func(chunk) >= target - 1) {
                chunk = operations[operation].func(chunk);
                operations[operation].count++;
            }

            if (operations[operation].count > 0) {
                chunk = transportingAndWashing(chunk);
                console.log(`${operation} x${operations[operation].count}`);
                console.log('Transporting and washing');
            }

            operations[operation].count = 0;
        }

        if (chunk === target - 1) {
            chunk = xRay(chunk);
            console.log('X-ray x1');
        }

        console.log(`Finished crystal ${chunk} microns`);
    }
}

// Task 5
function dNA(num) {
    let patterns = [
        (x) => `**${x[0]}${x[1]}**`,
        (x) => `*${x[0]}--${x[1]}*`,
        (x) => `${x[0]}----${x[1]}`,
        (x) => `*${x[0]}--${x[1]}*`,
    ];
    let letters = [['A', 'T'], ['C', 'G'], ['T', 'T'], ['A', 'G'], ['G', 'G']]

    let patternsCount = 0;
    let lettersCount = 0;

    while (num > 0) {
        console.log(patterns[patternsCount](letters[lettersCount]));

        num--;
        patternsCount++;
        lettersCount++;

        if (patternsCount >= patterns.length) patternsCount = 0;
        if (lettersCount >= letters.length) lettersCount = 0;
    }
}
