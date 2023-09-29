gifts = input().split(" ")

while True:
    first_command = input()
    if first_command == "No Money":
        break
    second_command = first_command.split(" ")
    if "OutOfStock" in second_command:
        for i in range(len(gifts)):
            if second_command[1] == gifts[i]:
                gifts[i] = "None"
    elif "Required" in second_command:
        if 0 <= int(second_command[2]) < len(gifts):
            gifts[int(second_command[2])] = second_command[1]
    elif "JustInCase" in second_command:
        gifts[-1] = second_command[1]

for y in range(len(gifts)):
    if y < len(gifts) - 1:
        if gifts[y] != "None":
            print(gifts[y], end=" ")
    else:
        if gifts[y] != "None":
            print(gifts[y], end="")
