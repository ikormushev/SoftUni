number = int(input())

plants = {}

for _ in range(number):
    plant_info = input().split("<->")
    plant_name = plant_info[0]
    plant_rarity = int(plant_info[1])
    if plant_name not in plants:
        plants[plant_name] = {}
        plants[plant_name]["rarity"] = plant_rarity
        plants[plant_name]["ratings"] = []
    else:
        plants[plant_name]["rarity"] = plant_rarity

while True:
    command = input()
    if command == "Exhibition":
        break
    invalid_plant = False
    action = command.split(" ")
    found_plant = action[1]

    if action[0] == "Rate:":
        rating = int(action[3])
        if found_plant in plants:
            plants[found_plant]["ratings"].append(rating)
        else:
            invalid_plant = True
    elif action[0] == "Update:":
        rarity = int(action[3])
        if found_plant in plants:
            plants[found_plant]["rarity"] = rarity
        else:
            invalid_plant = True
    elif action[0] == "Reset:":
        if found_plant in plants:
            plants[found_plant]["ratings"] = []
        else:
            invalid_plant = True

    if invalid_plant:
        print("error")

print("Plants for the exhibition:")
for (plant, info) in plants.items():
    if len(info["ratings"]) > 0:
        average_rating = sum(info["ratings"]) / len(info["ratings"])
    else:
        average_rating = 0
    print(f'- {plant}; Rarity: {info["rarity"]}; Rating: {average_rating:.2f}')
