def printing_names(names: list):
    blacklisted_count = names.count("Blacklisted")
    print(f"Blacklisted names: {blacklisted_count}")
    lost_count = names.count("Lost")
    print(f"Lost names: {lost_count}")

    for i in range(len(names)):
        if i == len(names) - 1:
            print(names[i])
        else:
            print(names[i], end=" ")


friends = input().split(", ")

while True:
    command = input()
    if command == "Report":
        break
    maintenance_command = command.split(" ")

    if "Blacklist" in maintenance_command:
        name = maintenance_command[1]
        if name in friends:
            name_index = friends.index(name)
            friends[name_index] = "Blacklisted"
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")

    elif "Error" in maintenance_command:
        name_index = int(maintenance_command[1])
        if 0 <= name_index < len(friends):
            if friends[name_index] not in ["Blacklisted", "Lost"]:
                name = friends[name_index]
                friends[name_index] = "Lost"
                print(f"{name} was lost due to an error.")

    elif "Change" in maintenance_command:
        new_name = maintenance_command[2]
        name_index = int(maintenance_command[1])
        if 0 <= name_index < len(friends):
            name = friends[name_index]
            friends[name_index] = new_name
            print(f"{name} changed his username to {new_name}.")

printing_names(friends)
