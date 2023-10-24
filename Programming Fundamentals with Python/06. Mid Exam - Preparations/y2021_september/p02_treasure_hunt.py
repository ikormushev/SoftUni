initial_loot = input().split("|")

while True:
    command = input()
    if command == "Yohoho!":
        break

    treasure_command = command.split(" ")
    if "Loot" in treasure_command:
        for i in range(1, len(treasure_command)):
            if treasure_command[i] not in initial_loot:
                initial_loot.insert(0, treasure_command[i])

    elif "Drop" in treasure_command:
        loot_position = int(treasure_command[1])
        if loot_position > len(initial_loot):
            continue
        loot_to_drop = initial_loot[loot_position]
        initial_loot.pop(loot_position)
        initial_loot.append(loot_to_drop)

    elif "Steal" in treasure_command:
        stolen_items = []
        steal_count = int(treasure_command[1])
        if steal_count > len(initial_loot):
            steal_count = len(initial_loot)
        for y in range(len(initial_loot[-steal_count:])):
            stolen_items.append(initial_loot[-steal_count+y])
            # in order to not change the list's length, we just change the item to "" and later remove it
            initial_loot[-steal_count+y] = ""

        for z in range(len(stolen_items)):
            if z == len(stolen_items) - 1:
                print(stolen_items[z])
            else:
                print(stolen_items[z], end=", ")

        for _ in range(initial_loot.count("")):
            initial_loot.remove("")

if len(initial_loot) > 0:
    items_length = [len(x) for x in initial_loot]
    average_gain = sum(items_length) / len(initial_loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
