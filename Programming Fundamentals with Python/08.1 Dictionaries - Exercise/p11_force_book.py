
force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    force_command = command
    is_user_found = False
    if " | " in force_command:
        force_command = force_command.split(" | ")
        force_side = force_command[0]
        force_user = force_command[1]

        for name in force_book.values():
            if force_user in name:
                is_user_found = True
                break

        if not is_user_found:
            if force_side in force_book:
                force_book[force_side].append(force_user)
            else:
                force_book[force_side] = [force_user]

    elif " -> " in force_command:
        force_command = force_command.split(" -> ")
        force_user = force_command[0]
        force_side = force_command[1]

        for (user_side, user_names) in force_book.items():
            if force_user in user_names:
                for name in user_names:
                    if name == force_user:
                        user_names.remove(name)
                break

        if force_side in force_book:
            force_book[force_side].append(force_user)
        else:
            force_book[force_side] = [force_user]

        print(f"{force_user} joins the {force_side} side!")

for (side, users) in force_book.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
