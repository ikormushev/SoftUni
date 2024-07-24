// Task 1
function solve(num) {
    console.log(num * 2);
}

// Task 2
function printName(name, age, avgGrade) {
    console.log(`Name: ${name}, Age: ${age}, Grade: ${avgGrade.toFixed(2)}`);
}

// Task 3
function checkGrade(grade) {
    let result = undefined;

    if (grade >= 5.50) {
        result = "Excellent";
    } else {
        result = "Not excellent";
    }

    console.log(result);
}

// Task 4
function monthPrinter(number) {
    let result = undefined;

    switch (number) {
        case 1:
            result = "January";
            break;
        case 2:
            result = "February";
            break;
        case 3:
            result = "March";
            break;
        case 4:
            result = "April";
            break;
        case 5:
            result = "May";
            break;
        case 6:
            result = "June";
            break;
        case 7:
            result = "July";
            break;
        case 8:
            result = "August";
            break;
        case 9:
            result = "September";
            break;
        case 10:
            result = "October";
            break;
        case 11:
            result = "November";
            break;
        case 12:
            result = "December";
            break;
        default:
            result = "Error!";
    }

    console.log(result);
}

// Task 5
function mathOperations(number1, number2, operation) {
    let operations = {
        "+": (a, b) => a + b,
        "-": (a, b) => a - b,
        "*": (a, b) => a * b,
        "/": (a, b) => a / b,
        "%": (a, b) => a % b,
        "**": (a, b) => a ** b,
    };

    console.log(operations[operation](number1, number2));
}

// Task 6
function findMaxNum(...numbers) {
    let largestNum = numbers[0];
    for (let num of numbers) {
        if (num > largestNum) {
            largestNum = num;
        }
    }
    console.log(`The largest number is ${largestNum}.`);
}

// Task 7
function getTicketPrice(dayType, age) {
    function checkPrices(firstPrice, secondPrice, thirdPrice) {
        if (age >= 0 && age <= 18) {
            return `${firstPrice}$`
        } else if (age > 18 && age <= 64) {
            return `${secondPrice}$`
        } else if (age > 64 && age <= 122) {
            return `${thirdPrice}$`
        } else {
            return "Error!"
        }
    }

    let days = {
        "Weekday": checkPrices(12, 18, 12),
        "Weekend": checkPrices(15, 20, 15),
        "Holiday": checkPrices(5, 12, 10),
    };

    console.log(days[dayType]);
}

// Task 8
function circleArea(argument) {
    if (typeof argument === 'number') {
        console.log((Math.PI * (argument ** 2)).toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeof argument}.`)
    }
}

// Task 9
function printNumbers() {
    for (let i = 1; i < 6; i++) {
        console.log(i);
    }
}

// Task 10
function printNumbersFromMToN(m, n) {
    for (let i = m; i >= n; i--) {
        console.log(i);
    }
}
