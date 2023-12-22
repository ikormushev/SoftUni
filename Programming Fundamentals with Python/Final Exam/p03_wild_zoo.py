animals = {}
animals_by_area = {}

while True:
    action = input()
    if action == "EndDay":
        break
    command = action.split(" ")
    information = (command[1]).split("-")
    animal_name = information[0]

    if command[0] == "Add:":
        needed_food_quantity = int(information[1])
        area = information[2]

        if animal_name not in animals:
            animals[animal_name] = {}
            animals[animal_name]["food"] = needed_food_quantity
            animals[animal_name]["area"] = area
        else:
            animals[animal_name]["food"] += needed_food_quantity

        if area not in animals_by_area:
            animals_by_area[area] = {}
            animals_by_area[area][animal_name] = needed_food_quantity
        else:
            if animal_name not in animals_by_area[area]:
                animals_by_area[area][animal_name] = needed_food_quantity
            else:
                animals_by_area[area][animal_name] += needed_food_quantity

    elif command[0] == "Feed:":
        food = int(information[1])
        if animal_name in animals:
            animals[animal_name]["food"] -= food
            area = animals[animal_name]["area"]
            animals_by_area[area][animal_name] -= food
            if animals[animal_name]["food"] <= 0:
                del animals[animal_name]
                del animals_by_area[area][animal_name]
                print(f"{animal_name} was successfully fed")

print("Animals:")
for (name, info) in animals.items():
    print(f" {name} -> {animals[name]['food']}g")

print("Areas with hungry animals:")
for (given_area, info) in animals_by_area.items():
    if len(info) != 0:
        print(f" {given_area}: {len(info)}")