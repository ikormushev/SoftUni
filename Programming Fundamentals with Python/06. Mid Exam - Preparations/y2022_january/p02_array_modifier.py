def printing_integers(numbers: list):
    for y in range(len(numbers)):
        if y == len(numbers) - 1:
            print(numbers[y])
        else:
            print(numbers[y], end=", ")


integers = list(map(int, input().split(" ")))

while True:
    command = input()
    if command == "end":
        break
    modifying_command = command.split(" ")
    if "swap" in modifying_command:
        first_index = int(modifying_command[1])
        second_index = int(modifying_command[2])
        integers[first_index], integers[second_index] = integers[second_index], integers[first_index]

    elif "multiply" in modifying_command:
        first_index = int(modifying_command[1])
        second_index = int(modifying_command[2])
        integers[first_index] *= integers[second_index]

    elif "decrease" in modifying_command:
        for i in range(len(integers)):
            integers[i] -= 1

printing_integers(integers)
