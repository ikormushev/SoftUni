pirate_ship_status = list(map(int, input().split(">")))
warship_status = list(map(int, input().split(">")))
maximum_health_capacity = int(input())

pirate_ship_sunken = False

while True:
    if pirate_ship_sunken:
        break

    command = input()
    if command == "Retire":
        print(f"Pirate ship status: {sum(pirate_ship_status)}")
        print(f"Warship status: {sum(warship_status)}")
        break

    new_command = command.split(" ")
    if "Fire" in new_command:
        fire_index = int(new_command[1])
        fire_damage = int(new_command[2])
        if fire_index >= len(warship_status) or fire_index < 0:
            continue
        warship_status[fire_index] -= fire_damage
        if warship_status[fire_index] <= 0:
            print("You won! The enemy ship has sunken.")
            break

    elif "Defend" in new_command:
        temporary_end_index = 0
        defend_start_index = int(new_command[1])
        defend_end_index = int(new_command[2])
        warship_damage = int(new_command[3])
        if defend_start_index < 0 or defend_end_index >= len(pirate_ship_status):
            continue

        for i in range(len(pirate_ship_status[defend_start_index:defend_end_index + 1])):
            pirate_ship_status[defend_start_index + i] -= warship_damage
            if pirate_ship_status[defend_start_index + i] <= 0:
                print("You lost! The pirate ship has sunken.")
                pirate_ship_sunken = True
                break

    elif "Repair" in new_command:
        repair_index = int(new_command[1])
        repair_health = int(new_command[2])
        if repair_index >= len(pirate_ship_status) or repair_index < 0:
            continue

        if pirate_ship_status[repair_index] + repair_health > maximum_health_capacity:
            repair_health = maximum_health_capacity - pirate_ship_status[repair_index]
            pirate_ship_status[repair_index] = maximum_health_capacity
        else:
            pirate_ship_status[repair_index] += repair_health

    elif "Status" in new_command:
        sections_for_repair = 0
        for y in range(len(pirate_ship_status)):
            if pirate_ship_status[y] < maximum_health_capacity * 0.20:
                sections_for_repair += 1
        print(f"{sections_for_repair} sections need repair.")
