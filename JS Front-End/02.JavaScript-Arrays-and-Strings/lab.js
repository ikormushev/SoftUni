// Task 1
function sumFirstAndLastArrayElements(arr) {
    console.log(arr[0] + arr[arr.length - 1]);
}

// Task 2
function reverseArrayOfNumbers(n, arr) {
    let newArr = arr.slice(0, n);
    newArr.reverse();
    console.log(newArr.join(' '));
}

// Task 3
function evenAndOddSubstraction(arr) {
    let totalSum = arr.reduce((x, y) => {
        return (y % 2 === 0) ? (x + y): x - y;
    }, 0);
    console.log(totalSum);
}

// Task 4 
function stringSubstring(text, n, m) {
    console.log(text.substring(n, n+m));
}

// Task 5
function censoredWords(text, word) {
    do {
        text = text.replace(word, "*".repeat(word.length))
    } while (text.includes(word));

    console.log(text);
}

// Task 6
function countStringOccurrences(text, search) {
    let splitText = text.split(" ").reduce((x, y) => {
            return (y === search) ? x + 1: x;
    }, 0)
    console.log(splitText);
}

