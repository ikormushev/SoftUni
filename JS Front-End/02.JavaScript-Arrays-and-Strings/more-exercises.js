// Task 1
function login(arr) {
    let username = arr[0];

    for (let i = 1; i < arr.length; i++) {
        let currTry = arr[i].split('').reverse().join('');
        if (currTry === username) {
            console.log(`User ${username} logged in.`);
            break;
        } else {
            if (i === 4) {
                console.log(`User ${username} blocked!`);
                break;
            }
            console.log(`Incorrect password. Try again.`);
        }
    }
}

// Task 2
function bitcoinMining(arr) {
    let prices = {
        "bitcoin": 11949.16,
        "gold": 67.51
    };

    let bitcoinsPurchased = 0;
    let dayOfFirstPurchase = 0;
    let moneyLeft = 0;

    for (let i = 0; i < arr.length; i++) {
        let goldMined = arr[i];

        if ((i+1) % 3 === 0) {
            goldMined *= 0.70;
        }

        moneyLeft += goldMined * prices["gold"];
        
        while (moneyLeft - prices["bitcoin"] >= 0) {
            if (bitcoinsPurchased === 0) {
                dayOfFirstPurchase = i+1;
            }

            bitcoinsPurchased += 1;
            moneyLeft -= prices["bitcoin"];
        }
    }

    console.log(`Bought bitcoins: ${bitcoinsPurchased}`);
    if (bitcoinsPurchased > 0) {
        console.log(`Day of the first purchased bitcoin: ${dayOfFirstPurchase}`);
    }

    console.log(`Left money: ${moneyLeft.toFixed(2)} lv.`);
}

// Task 3
function pyramidOfKingDjoser(base, increment) {
    let stone = 0;
    let marble = 0;
    let lapis = 0;
    let gold = 0;

    let currentWidth = base;
    let currentLength = base;
    let step = 1;

    while (currentWidth > 0 && currentLength > 0) {
        let totalArea = currentWidth * currentLength;
        
        if (currentWidth < 3 && currentLength < 3) {
            gold += totalArea * increment;
            break;
        }

        let innerArea = (currentWidth - 2) * (currentLength - 2);
        stone += innerArea * increment;

        let outerArea = 2 * (currentWidth + currentLength - 2);

        if (step % 5 === 0) {
            lapis += outerArea * increment;
        } else {
            marble += outerArea * increment;
        }

        currentWidth -= 2;
        currentLength -= 2;
        step++;
    }

    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapis)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${Math.floor(step * increment)}`);
}
