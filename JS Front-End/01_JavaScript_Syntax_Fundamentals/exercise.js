// Task 1
function ageDeterminator(age) {
    let result = "";

    if (age >= 0 && age <= 2) {
        result = "baby";
    } else if (age >= 3 && age <= 13) {
        result = "child";
    } else if (age >= 14 && age <= 19) {
        result = "teenager";
    } else if (age >= 20 && age <= 65) {
        result = "adult";
    } else if (age >= 66) {
        result = "elder";
    } else {
        result = "out of bounds";
    }

    console.log(result);
}

// Task 2
function vacation(peopleNum, groupType, day) {
    function priceSetters(price1, price2, price3) {
        switch (day) {
            case "Friday":
                return price1
            case "Saturday":
                return price2;
            case "Sunday":
                return price3;
        }
    }

    let offers = {
        "Students": priceSetters(8.45, 9.80, 10.46),
        "Business": priceSetters(10.90, 15.60, 16),
        "Regular": priceSetters(15, 20, 22.50),
    }

    let price = offers[groupType];
    let totalPrice = price * peopleNum;

    if (groupType === "Students" && peopleNum >= 30) {
        totalPrice *= 0.85;
    } else if (groupType === "Business" && peopleNum >= 100) {
        totalPrice -= price * 10;
    } else if (groupType === "Regular" && (peopleNum >= 10 && peopleNum <= 20)) {
        totalPrice *= 0.95;
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}

// Task 3
function leapYear(year) {
    let result = "no";

    if (((year % 4 === 0) && (year % 100 != 0)) || (year % 400 === 0)) {
        result = "yes";
    }
    console.log(result);
}

// Task 4
function numbersSum(n, m) {
    let nSum = 0;
    let numbers = [];

    for (let i = n; i <= m; i++) {
        nSum += i;
        numbers.push(`${i}`);
    }

    console.log(`${numbers.join(' ')}\nSum: ${nSum}`);
}

// Task 5
function multiplicationTable(number) {
    for (let i = 1; i <= 10; i++) {
        console.log(`${number} X ${i} = ${number * i}`);
    }
}

// Task 6
function sumDigits(number) {
    let digitsSum = 0;

    for (let digit of String(number)) {
        digitsSum += Number(digit);
    }

    console.log(digitsSum);
}

// Task 7
function charsToString(...chars) {
    console.log(chars.join(''));
}

// Task 8
function reversedChars(...chars) {
    console.log(chars.reverse().join(' '));
}

// Task 9
function fruitPriceCheck(name, grams, pricePerKilo) {
    let kilos = grams / 1000;
    console.log(`I need $${(kilos * pricePerKilo).toFixed(2)} to buy ${kilos.toFixed(2)} kilograms ${name}.`);
}

// Task 10
function sameNumbers(number) {
    let digits = String(number);
    let digitsSum = 0;
    let sameDigits = true;

    for (let digit of digits) {
        digitsSum += Number(digit);
        if (digit !== digits[0]) {
            sameDigits = false;
        }
    }
    console.log(`${sameDigits}\n${digitsSum}`);
}

// Task 11
function roadRadar(speed, area) {
    let speedLimits = {
        "motorway": 130,
        "interstate": 90,
        "city": 50,
        "residential": 20
    };

    let speedLimit = speedLimits[area];

    if (speed <= speedLimit) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`)
    } else {
        let status = "speeding";
        let speeding = speed - speedLimit;
        if (speeding > 20 && speeding <= 40) {
            status = "excessive speeding";
        } else if (speeding > 40) {
            status = "reckless driving";
        }

        console.log(`The speed is ${speeding} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
    }
}

// Task 12
function cookingByNumbers(number, ...operations) {
    let num = Number(number);

    let operationsToDo = {
        chop: x => x / 2,
        dice: x => Math.sqrt(x),
        spice: x => x + 1,
        bake: x => x * 3,
        fillet: x => x * 0.8
    };

    for (let operation of operations) {
        num = operationsToDo[operation](num);
        console.log(num);
    }
}
