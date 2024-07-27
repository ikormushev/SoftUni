// Task 1
class Storage {
    constructor(capacity) {
        this.capacity = capacity;
        this.storage = [];
    }

    get totalCost() {
        return this.storage.reduce((x, y) => x + (y["price"] * y["quantity"]), 0);
    }
    addProduct(product) {
        this.storage.push(product);
        this.capacity -= product["quantity"];
    }

    getProducts() {
        return this.storage.map(x => JSON.stringify(x)).join("\n");
    }
}

// Task 2
function catalogue(arr) {
    let dictionary = {};

    for (let productInfo of arr) {
        let [name, price] = productInfo.split(" : ");
        let product = {name: name, price: price};

        let firstLetter = name[0].toUpperCase();

        if (!dictionary.hasOwnProperty(firstLetter)) dictionary[firstLetter] = [];

        dictionary[firstLetter].push(product);
    }

    let sortedDict = Object.entries(dictionary)
                    .sort((x, y) => x[0].localeCompare(y[0]))
                    .map(z => `${z[0]}\n${z[1]
                            .sort((x, y) => x.name.localeCompare(y.name))
                            .map(q => `  ${q.name}: ${q.price}`)
                        .join("\n")}`
                    );

    console.log(sortedDict.join("\n"));
}

// Task 3
class Laptop {
    constructor(info, quality) {
        this.info = info;
        this.quality = quality;
        this.isOn = false;
    }

    turnOn() {
        this.isOn = true;
        this.quality--;
    }

    turnOff() {
        this.isOn = false;
        this.quality--;
    }

    showInfo() {
        return JSON.stringify(this.info);
    }

    get price() {
        return 800 - (this.info.age * 2) + (this.quality * 0.5);
    }
}

// Task 4
function flightSchedule(arr) {
    let flights = {};
    let statusToCheck = arr[2][0];

    for (let flightInfo of arr[0]) {
        let [fligthNumber, ...destination] = flightInfo.split(" ");
        flights[fligthNumber] = {Destination: destination.join(" "), Status: ""};
    }

    for (let flightInfo of arr[1]) {
        let [fligthNumber, ...status] = flightInfo.split(" ");
        if (flights.hasOwnProperty(fligthNumber)) flights[fligthNumber].Status = status.join(" ");
    }

    let result = [];

    if (statusToCheck == "Ready to fly") {
        result = Object.entries(flights)
                .filter(x => x[1].Status == "");
        result.forEach(x => x[1].Status = statusToCheck);
    } else {
        result = Object.entries(flights)
                .filter(x => x[1].Status === "Cancelled");
    }
    result.forEach(x => console.log(x[1]));  
    
}

// Task 5
function schoolRegister(arr) {
    let nextGrades = {};
    let lowestScore = 3;

    for (let studentInfo of arr) {
        let [studentNameInfo, studentGradeInfo, studentAvgInfo] = studentInfo.split(", ");
        let studentName = studentNameInfo.split(": ")[1];
        let studentGrade = studentGradeInfo.split(": ")[1];
        let studentAvgScore = Number(studentAvgInfo.split(": ")[1]);

        if (studentAvgScore > lowestScore) {
            let nextGrade = String(Number(studentGrade) + 1);
            if (!nextGrades.hasOwnProperty(nextGrade)) {
                nextGrades[nextGrade] = {students: [], "avgAnnualGrade": 0};
            }

            nextGrades[nextGrade].students.push(studentName);
            nextGrades[nextGrade]["avgAnnualGrade"] += studentAvgScore;
        }
    }

    let result = Object.entries(nextGrades);
    result.forEach(x => x[1]["avgAnnualGrade"] = Number(x[1]["avgAnnualGrade"]) / x[1].students.length);
    result.sort((x, y) => Number(x) - Number(y));
    let newResult = result
                    .map(x => `${x[0]} Grade\nList of students: ${x[1].students.join(", ")}\nAverage annual score from last year: ${x[1]["avgAnnualGrade"].toFixed(2)}`);
    
    console.log(newResult.join("\n\n"));
}

// Task 6
function browserHistory(obj, strArr) {
    let isActionValid = false;

    for (let action of strArr) {
        let isActionValid = false;
        if (action.includes("Close")) {
            let siteName = action.split("Close ")[1];

            if (obj["Open Tabs"].includes(siteName)) {
                obj["Open Tabs"] = obj["Open Tabs"].filter(x => x !== siteName);
                obj["Recently Closed"].push(siteName);
                isActionValid = true;
            }
        } else if (action.includes("Open")) {
            let siteName = action.split("Open ")[1];
            obj["Open Tabs"].push(siteName);
            isActionValid = true;
        } else if (action === "Clear History and Cache") {
            obj["Open Tabs"] = [];
            obj["Recently Closed"] = [];
            obj["Browser Logs"] = [];
        }

        if (isActionValid === true) {
            obj["Browser Logs"].push(action);
        }
    }

    let result = [];

    for (let key in obj) {
        if (key === "Browser Name") result.push(obj[key]);
        else {
            result.push(`${key}: ${obj[key].join(", ")}`)
        }
    }
    console.log(result.join("\n"));
}

// Task 7
function sequences(strArrays) {
    let arrays = [];
    
    function areArraysEqual(arr1, arr2) {
        if (arr1.length !== arr2.length) return false;
    
        for (let i = 0; i < arr1.length; i++) {
            if (arr1[i] !== arr2[i]) return false;
        }

        return true;
    }

    for (let arr of strArrays) {
        let foundEqualArr = false;
        let numbers = arr.substring(1, arr.length - 1).split(", ").map(x => Number(x));

        numbers.sort((x, y) => y - x);

        for (let numArr of arrays) {
            foundEqualArr = areArraysEqual(numArr, numbers);

            if (foundEqualArr === true) break;
        }

        if (!foundEqualArr) arrays.push(numbers);
    }

    arrays.sort((x, y) => x.length - y.length);
    console.log(arrays.map(x => `[${x.join(", ")}]`).join("\n"));
}

// Task 8
function garage(arr) {
    let garageStorage = {};

    for (let garInfo of arr) {
        let [garageNum, properties] = garInfo.split(" - ");
        properties = properties.split(", ");
        let newCar = {};

        for (let propertyInfo of properties) {
            let [propertyName, propertyValue] = propertyInfo.split(": ");

            newCar[propertyName] = propertyValue;
        }

        if (!garageStorage.hasOwnProperty(garageNum)) garageStorage[garageNum] = [];

        let carString = Object.entries(newCar).map(x => `${x[0]} - ${x[1]}`).join(", ");
        garageStorage[garageNum].push(`--- ${carString}`);
    }

    let result = Object.entries(garageStorage);
    result.sort((x, y) => Number(x[0]) - Number(y[0]));
    result = result.map(x => `Garage № ${x[0]}\n${x[1].join("\n")}`).join("\n");

    console.log(result);
}

// Task 9
function armies(arr) {
    let leadersArmies = {};

    for (let info of arr) {
        if (info.includes("arrives")) {
            let leaderName = info.split(" arrives")[0];

            leadersArmies[leaderName] = [];
        } else if (info.includes("defeated")) {
            let leaderName = info.split(" defeated")[0];

            if (leadersArmies.hasOwnProperty(leaderName)) {
                delete leadersArmies[leaderName];
            }
        } else if (info.match(/: [a-zA-z]+ *[a-zA-Z]*, \d+/) !== null) {
            let [leardeName, armyInfo] = info.split(": ");
            let [armyName, armyCount] = armyInfo.split(", ");

            if (leadersArmies.hasOwnProperty(leardeName)) {
                leadersArmies[leardeName].push({name: armyName, count: Number(armyCount)});
            }
        } else if (info.includes(" + ")) {
            let [armyName, armyCount] = info.split(" + ");
            armyCount = Number(armyCount);

            Object.entries(leadersArmies).forEach(x => x[1].forEach(y => ((y.name === armyName) ? y.count += armyCount: y)));
        }
    }

    for (let leader in leadersArmies) {
        leadersArmies[leader] = {"totalArmyCount": 0, "armies": leadersArmies[leader]};
        leadersArmies[leader]["totalArmyCount"] = leadersArmies[leader]["armies"].reduce((x, y) => x + y.count, 0);
        leadersArmies[leader]["armies"].sort((x, y) => y.count - x.count);
        leadersArmies[leader]["armies"] = leadersArmies[leader]["armies"].map(y => `>>> ${y.name} - ${y.count}`);
    }

    let leadersToSort = Object.entries(leadersArmies);
    leadersToSort.sort((x, y) => y[1]["totalArmyCount"] - x[1]["totalArmyCount"]);
    let result = leadersToSort
            .map(x => `${x[0]}: ${x[1]["totalArmyCount"]}\n${x[1]["armies"].join("\n")}`).join("\n");

    console.log(result);
}

// Task 10
function comments(arr) {
    let users = [];
    let articles = {};

    for (let info of arr) {
        if (info.includes("user ")) {
            let username = info.split(" ")[1];

            users.push(username);
        } else if (info.includes("article ")) {
            let artcile = info.split(" ")[1];

            articles[artcile] = [];

        } else if (info.includes(" posts on ")) {
            let [usernameAndArticle, commentInfo] = info.split(": ");

            let [username, article] = usernameAndArticle.split(" posts on ");
            let [commentTitle, commentContent] = commentInfo.split(", ");

            if (users.includes(username) && articles.hasOwnProperty(article)) {
                articles[article].push({"user": username, "commentTitle": commentTitle, "commentContent": commentContent});
            }
        }
    }

    let articlesToSort = Object.entries(articles);
    articlesToSort.sort((x, y) => y[1].length - x[1].length);
    articlesToSort.forEach(x => x[1].sort((y, z) => y.user.localeCompare(z.user)));
    let newArticles = articlesToSort.map(x => [x[0], x[1].map(y => `--- From user ${y.user}: ${y.commentTitle} - ${y.commentContent}`)]);

    let result = newArticles.map(x => `Comments on ${x[0]}\n${x[1].join("\n")}`).join("\n");
    console.log(result);
}

// Task 11
function bookShelf(arr) {
    let booksGenres = {};

    for (let info of arr) {
        if (info.includes(" -> ")) {
            let [shelfID, shelfGenre] = info.split(" -> ");

            if (!booksGenres.hasOwnProperty(shelfID)) {
                booksGenres[shelfID] = {"genreType": shelfGenre, "genreBooks": []};
            }
        } else if (info.match(/(?:\b[a-zA-Z]+\b\s*)+: (?:\b[a-zA-Z]+\b\s*)+, [a-zA-Z]+/) !== null) {
            let [bookTitle, secondInfo] = info.split(": ");
            let [bookAuthor, bookGenre] = secondInfo.split(", ");
            let book = {"title": bookTitle, "author": bookAuthor};
            let genreIDName = Object.entries(booksGenres).find(x => x[1].genreType === bookGenre);
            if (genreIDName !== undefined) {
                genreIDName[1]["genreBooks"].push(book);
            }
        }
    }

    let books = Object.entries(booksGenres);
    books.sort((x, y) => y[1]["genreBooks"].length - x[1]["genreBooks"].length);
    books.forEach((x => x[1]["genreBooks"].sort((y, z) => y.title.localeCompare(z.title))));

    let result = books.map((x => {
        let stringedBooks = x[1]["genreBooks"].map(z => `--> ${z.title}: ${z.author}`);
        return `${x[0]} ${x[1]["genreType"]}: ${x[1]["genreBooks"].length}\n${stringedBooks.join("\n")}`;
    }));

    console.log(result.join("\n"));
}

// Task 12
function softUniStudents(arr) {
    let courses = {};

    for (let info of arr) {
        let match = info.match(/(\b[a-zA-Z#\.]+\b\s*)+: (\d+)/);
        if (match !== null) {
            let courseName = match[1];
            let courseCapacity = Number(match[2]);

            if (!courses.hasOwnProperty(courseName)) {
                courses[courseName] = {
                    "capacity": 0,
                    "students": []
                };
            }

            courses[courseName].capacity += courseCapacity;
            continue;
        } 

        match = info.match(/([a-zA-Z0-9_ ]+)\[(\d+)\] with email ([a-zA-Z0-9\._%+-@]+) joins ([a-zA-Z0-9 #\.]+)/);
        if (match !== null) {
            let username = match[1];
            let credits = Number(match[2]);
            let email = match[3];
            let courseName = match[4];
        
            let student = {"username": username, "credits": credits,"email": email};
    
            if (courses.hasOwnProperty(courseName)) {
                if (courses[courseName].capacity > courses[courseName].students.length) {
                    courses[courseName].students.push(student);
                }
            }
        }
    }

    let coursesToSort = Object.entries(courses);
    coursesToSort.sort((x, y) => y[1].students.length - x[1].students.length);
    coursesToSort.forEach(x => x[1].students.sort((y, z) => z.credits - y.credits));

    let result = coursesToSort.map(x => {
        let students = x[1].students.map(y => `--- ${y.credits}: ${y.username}, ${y.email}`);
        let newResult = [`${x[0]}: ${x[1].capacity - x[1].students.length} places left`];
        if (students.length > 0) {
            newResult.push(students.join("\n"));
        }
        return newResult.join("\n");
    });

    console.log(result.join("\n"));
}
