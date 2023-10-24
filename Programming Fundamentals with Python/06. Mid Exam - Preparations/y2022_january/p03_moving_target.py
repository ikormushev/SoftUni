def printing_targets(targets: list):
    for y in range(len(targets)):
        if y == len(targets) - 1:
            print(targets[y])
        else:
            print(targets[y], end="|")


targets_values = list(map(int, input().split(" ")))

while True:
    command = input()
    if command == "End":
        printing_targets(targets_values)
        break

    manipulating_command = command.split(" ")
    index = int(manipulating_command[1])
    action = int(manipulating_command[2])

    if "Shoot" in manipulating_command:
        if 0 <= index < len(targets_values):
            targets_values[index] -= action
            if targets_values[index] <= 0:
                targets_values.pop(index)

    elif "Add" in manipulating_command:
        if 0 <= index < len(targets_values):
            targets_values.insert(index, action)
        else:
            print("Invalid placement!")

    elif "Strike" in manipulating_command:
        if 0 <= index < len(targets_values):
            start_index = index - action
            end_index = index + action
            if start_index < 0 or end_index >= len(targets_values):
                print("Strike missed!")
                continue
            for i in range(len(targets_values[start_index:end_index + 1])):
                targets_values[start_index + i] = ""
            for _ in range(targets_values.count("")):
                targets_values.remove("")
        else:
            print("Strike missed!")
