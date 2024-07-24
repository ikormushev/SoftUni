// Task 1
function arrayRotation(arr, num) {
    for (let i = 0; i < num; i++) {
        arr.push(arr.shift());
    }

    console.log(arr.join(' '));
}

// Task 2
function printEveryNthElementFromArray(arr, num) {
    let newArr = [];
    let index = 0;

    while (index < arr.length) {
        newArr.push(arr[index]);
        index += num;
    }

    return newArr;
}

// Task 3
function listOfName(arr) {
    arr.sort((x, y) => x.localeCompare(y));

    for (let i = 0; i < arr.length; i++) {
        console.log(`${i+1}.${arr[i]}`)
    }
}

// Task 4
function sortingNumbers(arr) {
    let newArr = [];
    arr.sort((x, y) => x - y);

    for (let i = 0; i < arr.length / 2; i++) {
        newArr.push(arr[i]);
        newArr.push(arr[arr.length - 1 - i]);
    }

    if (arr.length % 2 === 1) {
        newArr.pop();
    }
    return newArr;
}

// Task 5
function revealWord(words, text) {
    let replacements = words.split(", ");

    let starMatches = text.match(/\*+/g) || [];
    let newStrings = [];

    for (let i = 0; i < starMatches.length; i++) {
        for (let j = 0; j < replacements.length; j++) {
            if (starMatches[i].length == replacements[j].length) {
                text = text.replace(starMatches[i], replacements[j]);
            }
        }
    }

    return text;
}

// Task 6
function modernTimeOfHashTag(text) {
    let specialWords = text.match(/#[a-zA-Z]+\b/g).map(x => x.substring(1)) || [];

    console.log(specialWords.join("\n"));
}

// Task 7
function stringSubstring(word, text) {
    let newWord = word.toLowerCase();
    let newText = text.toLowerCase();

    let result = newText.includes(newWord) ? word: `${word} not found!`;
    console.log(result);
}

// Task 8
function stringSubstring(word, text) {
    let regex = new RegExp(`\\b${word}\\b`, 'i');

    let result = regex.test(text) ? word: `${word} not found!`
    console.log(result);
}

// Task 9
function pascalCaseSplitter(text) {
    let splitText = text.match(/[A-Z][a-z]*/g) || [];
    console.log(splitText.join(', '));
}
