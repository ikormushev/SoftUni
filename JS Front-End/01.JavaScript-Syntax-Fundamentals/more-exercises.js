// Task 1
function validityChecker(x1, y1, x2, y2) {
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

// Task 2
function wordsUppercase(text) {
    const words = text.match(/\w+/g);
    const upperCaseWords = words.map(word => word.toUpperCase());

    console.log(upperCaseWords.join(', '));
}

// Task 3
function calculator(number, operator, anotherNumber) {
    let operations = {
        "+": (x, y) => x + y,
        "-": (x, y) => x - y,
        "/": (x, y) => x / y,
        "*": (x, y) => x * y,
    };

    let result = operations[operator](number, anotherNumber);
    console.log(result.toFixed(2));
}

// Task 4
function gladiatorExpress(lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let expenses = 0;

    for (let i = 1; i <= lostFights; i++) {
        if (i % 2 === 0) {
            expenses += helmetPrice;
        }

        if (i % 3 === 0) {
            expenses += swordPrice;
        }

        if (i % 6 === 0) {
            expenses += shieldPrice;
        }

        if (i % 12 === 0) {
            expenses += armorPrice;
        }
    }
    console.log(`Gladiator expenses: ${expenses.toFixed(2)} aureus`);
}

// Task 5
function spiceMustFlow(number) {
    let daysCount = 0;
    let totalSpice = 0;

    while (number >= 100) {

        totalSpice += number;
        daysCount += 1;
        number -= 10;
        
        if (totalSpice - 26 >= 0) {
            totalSpice -= 26;
        } else {
            totalSpice = 0;
        }
    }
    if (totalSpice - 26 >= 0) {
        totalSpice -= 26;
    }
    console.log(daysCount);
    console.log(totalSpice);
}

