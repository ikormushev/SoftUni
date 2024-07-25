// Task 1
function smallestOfThreeNumbers(...numbers) {
    numbers.sort((x, y) => x - y);
    console.log(numbers[0]);
}

// Task 2
function addAndSubtract(x, y, z) {
    function sum() {
        return x + y;
    }
    
    function subtract() {
        return sum() - z;
    }

    console.log(subtract());
}

// Task 3
function charactersInRange(char1, char2) {
    let result = [];
    let firstAsciiValue = char1.charCodeAt(0);
    let secondAsciiValue = char2.charCodeAt(0);

    if (firstAsciiValue < secondAsciiValue) {
        for (let i = firstAsciiValue + 1; i < secondAsciiValue; i++) {
            result.push(String.fromCharCode(i));
        }
   } else {
        for (let i = secondAsciiValue + 1; i < firstAsciiValue; i++) {
            result.push(String.fromCharCode(i));
        }
   }

   console.log(result.join(' '));
}

// Task 4
function oddAndEvenSum(number) {
    let numberString = String(number);
    let oddSum = 0;
    let evenSum = 0;

    for (let i = 0; i < numberString.length; i++) {
        let curr = numberString[i];
        if (curr % 2 == 0) evenSum += Number(curr);
        else oddSum += Number(curr);
    }

    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`
}

// Task 5
function palindromeIntegers(arr) {
    let palindromes = [];

    for (let number of arr) {
        let curr = String(number);
        let reversedCurr = curr.split('').reverse().join('');

        palindromes.push(curr === reversedCurr);
    }

    console.log(palindromes.join('\n'));
}

// Task 6
function passwordValidator(pass) {
    let isValid = true;

    if (pass.length < 6 || pass.length > 10) {
        isValid = false;
        console.log("Password must be between 6 and 10 characters");
    }

    let lettersDigitsCount = pass.match(/[a-zA-Z0-9]/g) || [];

    if (lettersDigitsCount.length != pass.length) {
        isValid = false;
        console.log("Password must consist only of letters and digits");
    }

    let digitsCount = pass.match(/[0-9]/g) || [];

    if (digitsCount.length < 2) {
        isValid = false;
        console.log("Password must have at least 2 digits");
    }

    if (isValid === true) {
        console.log("Password is valid");
    }
}

// Task 7
function nXNMatrix(n) {
    let matrix = [];

    for (let i = 0; i < n; i++) {
        matrix[i] = `${String(n)} `.repeat(n).trimEnd().split('').join('');
    }

    console.log(matrix.join("\n"));
}

// Task 8
function perfectNumber(num) {
    let properDivisors = [];

    for (let i = 1; i < num; i++) {
        if (num % i === 0 ) {
            properDivisors.push(i);
        }
    }

    let divisorsSum = properDivisors.reduce((x, y) => x + y);

    let result = (num === divisorsSum) ? "We have a perfect number!": "It's not so perfect.";

    console.log(result);
}

// Task 9
function loadingBar(number) {
    let percentages = '[' + '%'.repeat(number / 10) + '.'.repeat(10 - (number / 10)) + ']';

    if (number === 100) {
        console.log("100% Complete!");
        console.log(percentages)
    } else {
        console.log(`${number}% ${percentages}`)
        console.log("Still loading...");
    }
}

// Task 10
function factorialDivision(n, m) {
    function factorial(x) {
        if (x === 0 || x === 1) {
            return 1;
        }
        return x * factorial(x-1);
    }

    let firstFactorial = factorial(n);
    let secondFactorial = factorial(m);

    console.log((firstFactorial / secondFactorial).toFixed(2));
}
