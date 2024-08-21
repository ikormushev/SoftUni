function solve(data) {
    let superheroesNum = data.shift();
    let superheroes = {};

    for (let i = 0; i < superheroesNum; i++) {
        let [name, power, energy] = data.shift().split('-');
        energy = Number(energy);
        superheroes[name] = {powers: power.split(','), energy: energy};
    }

    let nextCommand = "";

    while (nextCommand !== "Evil Defeated!") {
        nextCommand = data.shift();
        let [command, superheroName, ...info] = nextCommand.split(" * ");

        if (command === "Use Power") {
            let superheroPower = info[0];
            let superheroEnergyRequired = Number(info[1]);

            if (superheroes[superheroName].powers.includes(superheroPower) === true && superheroes[superheroName].energy - superheroEnergyRequired > 0) {
                superheroes[superheroName].energy -= superheroEnergyRequired;
                console.log(`${superheroName} has used ${superheroPower} and now has ${superheroes[superheroName].energy} energy!`);
            } else {
                console.log(`${superheroName} is unable to use ${superheroPower} or lacks energy!`);
            }
        } else if (command === "Train") {
            let trainingEnergy = Number(info[0]);

            if (superheroes[superheroName].energy === 100) {
                console.log(`${superheroName} is already at full energy!`);
            } else {
                if (superheroes[superheroName].energy + trainingEnergy > 100) {
                    trainingEnergy = 100 - superheroes[superheroName].energy;
                    superheroes[superheroName].energy = 100;
                } else {
                    superheroes[superheroName].energy += trainingEnergy;
                }

                console.log(`${superheroName} has trained and gained ${trainingEnergy} energy!`);
            }
        } else if (command === "Learn") {
            let newSuperpower = info[0];

            if (superheroes[superheroName].powers.includes(newSuperpower) === true) {
                console.log(`${superheroName} already knows ${newSuperpower}.`);
            } else {
                superheroes[superheroName].powers.push(newSuperpower);
                console.log(`${superheroName} has learned ${newSuperpower}!`);
            }
        }
        
    }

    let superheroesData = Object.entries(superheroes).map(details => `Superhero: ${details[0]}\n- Superpowers: ${details[1].powers.join(', ')}\n- Energy: ${details[1].energy}`);
    console.log(superheroesData.join('\n'));
}

solve([
        "3",
        "Iron Man-Repulsor Beams,Flight-80",
        "Thor-Lightning Strike,Hammer Throw-10",
        "Hulk-Super Strength-60",
        "Use Power * Iron Man * Flight * 30",
        "Train * Thor * 20",
        "Train * Hulk * 50",
        "Learn * Hulk * Thunderclap",
        "Use Power * Hulk * Thunderclap * 70",
        "Evil Defeated!"
    ])
