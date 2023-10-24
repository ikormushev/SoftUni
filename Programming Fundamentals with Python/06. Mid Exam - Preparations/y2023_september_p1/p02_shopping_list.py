def updating_shopping_list(update):
    item = update[1]
    if "Urgent" in update:
        if item not in initial_shopping_list:
            initial_shopping_list.insert(0, item)

    elif "Unnecessary" in update:
        if item in initial_shopping_list:
            initial_shopping_list.remove(item)

    elif "Correct" in update:
        if item in initial_shopping_list:
            item_index = initial_shopping_list.index(item)
            initial_shopping_list[item_index] = update[2]

    elif "Rearrange" in update:
        if item in initial_shopping_list:
            initial_shopping_list.remove(item)
            initial_shopping_list.append(item)


initial_shopping_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    modified_command = command.split(" ")
    updating_shopping_list(modified_command)

for i in range(len(initial_shopping_list)):
    if i == len(initial_shopping_list) - 1:
        print(initial_shopping_list[i])
    else:
        print(initial_shopping_list[i], end=", ")
