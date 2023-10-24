elements = input().split(" ")

moves_count = 0

while True:
    if len(elements) == 0:
        print(f"You have won in {moves_count} turns!")
        break
    command = input()
    if command == "end":
        if len(elements) != 0:
            print("Sorry you lose :(")
            for y in range(len(elements)):
                if y == len(elements) - 1:
                    print(elements[y])
                else:
                    print(elements[y], end=" ")
            break

    moves_count += 1
    indexes = list(map(int, command.split(" ")))

    if ((indexes[0] == indexes[1]) or
            ((indexes[0] >= len(elements)) or (indexes[0] < 0))
            or ((indexes[1] >= len(elements)) or (indexes[1] < 0))):
        new_element_index = int(len(elements) / 2)
        new_element = f"-{moves_count}a"
        elements.insert(new_element_index, new_element)
        elements.insert(new_element_index, new_element)
        print("Invalid input! Adding additional elements to the board")

    elif elements[indexes[0]] == elements[indexes[1]]:
        print(f"Congrats! You have found matching elements - {elements[indexes[0]]}!")
        elements[indexes[0]] = ""
        elements[indexes[1]] = ""
        for _ in range(elements.count("")):
            elements.remove("")
        continue
    else:
        print("Try again!")
        continue
