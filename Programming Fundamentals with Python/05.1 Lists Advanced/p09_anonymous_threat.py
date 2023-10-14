strings_line = input().split(" ")

while True:
    command = input()
    if command == "3:1":
        for z in range(len(strings_line)):
            print(strings_line[z], end=" ")
        break

    new_command = command.split(" ")
    if "merge" in new_command:
        concatenated_elements = ""
        start_index = int(new_command[1])
        end_index = int(new_command[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(strings_line):
            end_index = len(strings_line) - 1

        for i in range(start_index, end_index + 1):
            concatenated_elements += strings_line[i]
            strings_line[i] = ""
        strings_line.insert(start_index, concatenated_elements)

    elif "divide" in new_command:
        index = int(new_command[1])
        partitions = int(new_command[2])
        if index >= len(strings_line):
            index = len(strings_line) - 1

        wanted_element = list(strings_line[index])
        strings_line[index] = ""

        divider = len(wanted_element) // partitions

        for y in range(partitions):
            if y != partitions - 1:
                strings_line.insert(index, "".join(wanted_element[y * divider: (y+1) * divider]))
            else:
                strings_line.insert(index, "".join(wanted_element[y * divider:]))
            index += 1

    for _ in range(strings_line.count("")):
        strings_line.remove("")
