// Task 1
function formatGrade(grade) {
    let result = "";

    if (grade < 3.00) {
        console.log("Fail (2)");
        return;
    }
    else if (grade >= 3.00 && grade < 3.50) result = 'Poor';
    else if (grade >= 3.50 && grade < 4.50) result = 'Good';
    else if (grade >= 4.50 && grade < 5.50) result = 'Very good';
    else if (grade >= 5.50) result = 'Excellent';

    result += ` (${grade.toFixed(2)})`;
    console.log(result);
}

// Task 2
function mathPower(number, power) {
    console.log(number ** power);
}

// Task 3
function repeatString(text, number) {
    console.log(text.repeat(number));
}

// Task 4
function orders(product, quantity) {
    let productsPrices = {
        coffee: 1.50,
        water: 1.00,
        coke: 1.40,
        snacks: 2.00,
    };

    console.log((productsPrices[product] * quantity).toFixed(2));
}

// Task 5
function simpleCalculator(n, m, operation) {
    let operations = {
        multiply: (x, y) => x * y,
        divide: (x, y) => x / y,
        add: (x, y) => x + y,
        subtract: (x, y) => x - y,
    };

    console.log(operations[operation](n,m));
}

// Task 6
function signCheck(...numbers) {
    let negatives = numbers.filter(num => num < 0).length;

    if (negatives % 2 === 0) {
        console.log("Positive");
    } else {
        console.log("Negative");
    }
}
