all_stops = list(input())

while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {''.join(all_stops)}")
        break
    manipulating_command = command.split(":")
    action = manipulating_command[0]

    if action == "Add Stop":
        index = int(manipulating_command[1])
        stop = list(manipulating_command[2])
        if 0 <= index < len(all_stops):
            first_half = all_stops[:index]
            second_half = all_stops[index:]
            all_stops = first_half + stop + second_half

    elif action == "Remove Stop":
        start_index = int(manipulating_command[1])
        end_index = int(manipulating_command[2])
        if 0 <= start_index < len(all_stops) and 0 <= end_index < len(all_stops):
            indexes_to_remove = end_index - start_index
            for _ in range(indexes_to_remove + 1):
                all_stops.pop(start_index)

    elif action == "Switch":
        old_string = manipulating_command[1]
        new_string = manipulating_command[2]
        starting_string = "".join(all_stops)
        if old_string in starting_string:
            starting_string = starting_string.replace(old_string, new_string)
            all_stops = list(starting_string)

    print("".join(all_stops))
