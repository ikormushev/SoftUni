
targeted_cities = {}

while True:
    command = input()
    if command == "Sail":
        break
    info = command.split("||")
    city_name = info[0]
    city_population = int(info[1])
    city_gold = int(info[2])

    if city_name not in targeted_cities:
        targeted_cities[city_name] = {}
        targeted_cities[city_name]["population"] = city_population
        targeted_cities[city_name]["gold"] = city_gold
    else:
        targeted_cities[city_name]["population"] += city_population
        targeted_cities[city_name]["gold"] += city_gold

while True:
    command = input()
    if command == "End":
        break
    action = command.split("=>")
    town = action[1]
    if action[0] == "Plunder":
        people = int(action[2])
        gold = int(action[3])

        targeted_cities[town]["population"] -= people
        targeted_cities[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if targeted_cities[town]["population"] <= 0 or targeted_cities[town]["gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            del targeted_cities[town]

    elif action[0] == "Prosper":
        gold = int(action[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            continue
        targeted_cities[town]["gold"] += gold
        print(f'{gold} gold added to the city treasury. {town} now has {targeted_cities[town]["gold"]} gold.')

if targeted_cities:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for (city, stats) in targeted_cities.items():
        print(f'{city} -> Population: {targeted_cities[city]["population"]} citizens, '
              f'Gold: {targeted_cities[city]["gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
