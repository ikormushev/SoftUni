raw_activation_key = list(input())

while True:
    command = input()
    if command == "Generate":
        print(f"Your activation key is: {''.join(raw_activation_key)}")
        break
    instruction = command.split(">>>")

    if instruction[0] == "Contains":
        substring = instruction[1]
        raw_activation_key = "".join(raw_activation_key)
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
        raw_activation_key = list(raw_activation_key)

    elif instruction[0] == "Flip":
        case_change = instruction[1]
        start_index = int(instruction[2])
        end_index = int(instruction[3])
        if case_change == "Upper":
            raw_activation_key[start_index:end_index] = [x.upper() for x in raw_activation_key[start_index:end_index]]
        elif case_change == "Lower":
            raw_activation_key[start_index:end_index] = [x.lower() for x in raw_activation_key[start_index:end_index]]
        print("".join(raw_activation_key))

    elif instruction[0] == "Slice":
        start_index = int(instruction[1])
        end_index = int(instruction[2])
        indexes_to_remove = end_index - start_index
        for _ in range(indexes_to_remove):
            raw_activation_key.pop(start_index)
        print("".join(raw_activation_key))
