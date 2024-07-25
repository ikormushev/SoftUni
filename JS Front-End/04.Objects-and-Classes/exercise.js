// Task 1
function employees(arr) {
    class Employee {
        constructor(name, personalNumber) {
            this.name = name;
            this.personalNumber = personalNumber;
        }

        info() {
            console.log(`Name: ${this.name} -- Personal Number: ${this.personalNumber}`);
        }
    }

    for (let name of arr) {
        let employee = new Employee(name, name.length);
        employee.info();
    }
}

// Task 2
function towns(arr) {
    class Town {
        constructor(town, latitude, longitude) {
            this.town = town;
            this.latitude = Number(latitude).toFixed(2);
            this.longitude = Number(longitude).toFixed(2);
        }

        info() {
            console.log(`{ town: '${this.town}', latitude: '${this.latitude}', longitude: '${this.longitude}' }`);
        }
    }

    for (let townInfo of arr) {
        let [town, latitude, longitude] = townInfo.split(" | ");

        let newTown = new Town(town, latitude, longitude)
        newTown.info();
    }
}

// Task 3
function storeProvision(stockArr, productsArr) {
    let store = {};

    function addProductsToStore(arr) {
        for (let i = 0; i < arr.length; i += 2) {
            let product = arr[i];
            let quantity = Number(arr[i+1]);

            if (!store.hasOwnProperty(product)) store[product] = 0;
            store[product] += quantity;
        }
    }

    addProductsToStore(stockArr);
    addProductsToStore(productsArr);

    Object.entries(store).forEach((x) => console.log(`${x[0]} -> ${x[1]}`));
}

// Task 4
function movies(arr) {
    class Movie {
        constructor(name, director="", date="") {
            this.name = name;
            this.director = director;
            this.date = date;
        }
    }

    let allMovies = [];

    function findMovie(moviesArr, movieName) {
        return moviesArr.find(x => x.name === movieName);
    }

    for (let command of arr) {
        if (command.includes("addMovie")) {
            let movie = new Movie(command.replace("addMovie ", ""));
            allMovies.push(movie);
        } else if (command.includes("directedBy")) {
            let [movieName, director] = command.split(" directedBy ");
            let movieFound = allMovies.find(x => x.name === movieName);

            if (movieFound) movieFound.director = director;
        } else if (command.includes("onDate")) {
            let [movieName, date] = command.split(" onDate ");
            let movieFound = findMovie(allMovies, movieName);

            if (movieFound) movieFound.date = date;
        }
    }

    let filteredMovies = allMovies.filter(m => m.director != "" && m.date != "");
    filteredMovies.forEach(x => console.log(JSON.stringify(x)))
}

// Task 5
function inventory(arr) {
    class Hero {
        constructor(name, level, items=[]) {
            this.name = name,
            this.level = level;
            this.items = items;
        }

        info() {
            console.log(`Hero: ${this.name}\nlevel => ${this.level}\nitems => ${this.items}`);
        }
    }

    let heroes = [];

    for (let heroInfo of arr) {
        let [name, level, items] = heroInfo.split(" / ");

        let hero = new Hero(name, level, items);
        heroes.push(hero);
    }

    heroes.sort((x, y) => x.level - y.level);
    heroes.forEach(x => x.info());
}

// Task 6
function worldsTracker(arr) {
    let wantedWords = arr[0].split(" ");
    arr.shift();

    let wordsCounts = {};

    for (let word of wantedWords) {
        wordsCounts[word] = 0;
    }

    for (let word of arr) {
        if (wantedWords.includes(word)) wordsCounts[word]++;
    }

    console.log(Object
                .entries(wordsCounts)
                .sort((x, y) => y[1] - x[1])
                .map(z => `${z[0]} - ${z[1]}`)
                .join("\n")
    );
}

// Task 7
function oddOccurrences(text) {
    let words = text.split(" ");
    let loweredWords = words.map(x => x.toLowerCase());

    let wordsTimes = {};

    for (let word of loweredWords) {
        if (!wordsTimes.hasOwnProperty(word)) wordsTimes[word] = 0;
        wordsTimes[word]++;
    }

    let filteredWords = Object.entries(wordsTimes)
                        .filter(x => x[1] % 2 === 1)
                        .map(x => x[0]);
    
    console.log(filteredWords.join(" "));
}

// Task 8
function piccolo(arr) {
    let parkingLot = {};

    for (let lotInfo of arr) {
        let [direction, carNumber] = lotInfo.split(", ");

        parkingLot[carNumber] = direction;

        if (direction === "OUT") delete parkingLot[carNumber];
    }

    let sortedOnlyNumbers = Object.entries(parkingLot).map(x => x[0]).sort((x, y) => x.localeCompare(y)) || [];
    if (sortedOnlyNumbers.length > 0) console.log(sortedOnlyNumbers.join("\n"));
    else console.log("Parking Lot is Empty");
}

// Task 9
function makeADictionary(arr) {
    let finalObject = {};

    for (let dict of arr) {
        let newObj = JSON.parse(dict);

        for (let key in newObj) {
            finalObject[key] = newObj[key];
        }
    }

    let result = Object.entries(finalObject)
                .sort((x, y) => x[0].localeCompare(y[0]))
                .map(z => `Term: ${z[0]} => Definition: ${z[1]}`);
    
    console.log(result.join("\n"));
}

// Task 10
class Vehicle {
    constructor(type, model, parts, fuel) {
        this.type = type;
        this.model = model;
        this.parts = parts;
        this.parts['quality'] = this.parts.engine * this.parts.power;
        this.fuel = fuel;
    }

    drive(fuelLoss) {
        this.fuel -= fuelLoss;
    }
}
