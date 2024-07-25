// Task 1
function personInfo(firstName, lastName, age) {
    return person = {
        firstName: firstName,
        lastName: lastName,
        age: age,
    };
}

// Task 2
function city(obj) {
    for (let key in obj) {
        console.log(`${key} -> ${obj[key]}`);
    }
}

// Task 3
function convertToObject(jSON) {
    let obj = JSON.parse(jSON);

    for (let key in obj) {
        console.log(`${key}: ${obj[key]}`);
    }
}

// Task 4
function convertToJSON(firstName, lastName, hairColor) {
    let obj = {
        name: firstName,
        lastName: lastName,
        hairColor: hairColor
    };
    
    let newJSON = JSON.stringify(obj);
    console.log(newJSON);
}

// Task 5
function phoneBook(arr) {
    let book = {};

    for (let info of arr) {
        info = info.split(" ");
        book[info[0]] = info[1];
    }

    let newBook = Object
                .entries(book)
                .map((x) => `${x[0]} -> ${x[1]}`);

    console.log(newBook.join('\n'));
}

// Task 6
function meetings(arr) {
    let weekDays = {};

    for (let info of arr) {
        let [day, name] = info.split(" ");
        if (weekDays.hasOwnProperty(day)) {
            console.log(`Conflict on ${day}!`);
        } else {
            weekDays[day] = name;
            console.log(`Scheduled for ${day}`);
        }
    }

    let final = Object
                .entries(weekDays)
                .map((x) => `${x[0]} -> ${x[1]}`);

    console.log(final.join('\n'));
}

// Task 7
function addressBook(arr) {
    let book = {};

    for (let info of arr) {
        let [name, address]= info.split(":");
        book[name] = address;
    }

    let newBook = Object
                .entries(book)
                .sort((x, y) => x[0].localeCompare(y[0]))
                .map((z) => `${z[0]} -> ${z[1]}`);

    console.log(newBook.join('\n'));
}

// Task 8
function cats(arr) {
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }

        meow() {
            console.log(`${this.name}, age ${this.age} says Meow`);
        }
    }

    for (let catInfo of arr) {
        let [name, age] = catInfo.split(" ");

        let cat = new Cat(name, age);
        cat.meow();
    }
}

// Task 9
function songs(arr) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }

    let allSongs = [];

    arr.shift();
    let typeSong = arr.pop();
    let printAllSongs = (typeSong === "all") ? true: false;

    for (let songInfo of arr) {
        let [typeList, name, time] = songInfo.split("_");

        let song = new Song(typeList, name, time);
        allSongs.push(song);
    }
    
    for (let song of allSongs) {
        if (printAllSongs === true || song.typeList === typeSong) {
            console.log(song.name)
        };
    }
}
