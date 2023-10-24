def printing_items(items: list):
    for y in range(len(items)):
        if y == len(items) - 1:
            print(items[y])
        else:
            print(items[y], end=", ")


journal = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        break

    update_command = command.split(" - ")
    if "Collect" in update_command:
        item = update_command[1]
        if item not in journal:
            journal.append(item)
    elif "Drop" in update_command:
        item = update_command[1]
        if item in journal:
            journal.remove(item)
    elif "Combine Items" in update_command:
        combining_items = update_command[1].split(":")
        if combining_items[0] in journal:
            old_item = combining_items[0]
            old_item_index = journal.index(old_item)
            new_item = combining_items[1]
            if old_item_index == len(journal) - 1:
                journal.append(new_item)
            else:
                journal.insert(old_item_index + 1, new_item)
    elif "Renew" in update_command:
        if update_command[1] in journal:
            item_index = journal.index(update_command[1])
            journal.pop(item_index)
            journal.append(update_command[1])

printing_items(journal)
