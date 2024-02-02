import os

command = input()

while command != "End":
    command_info = command.split("-")
    command_to_execute = command_info[0]
    file_name = command_info[1]
    file_path = os.path.join("files_used", file_name)

    if command_to_execute == "Create":
        with open(file_path, "w") as file:
            pass

    elif command_to_execute == "Add":
        content = command_info[2]
        with open(file_path, "a") as file:
            file.write(f"{content}\n")

    elif command_to_execute == "Replace":
        old_string = command_info[2]
        new_string = command_info[3]

        try:
            with open(file_path) as file:
                file_text = file.read()
                file_text = file_text.replace(old_string, new_string)

                file.seek(0)
                file.write(file_text)
                file.truncate()

        except FileNotFoundError:
            print("An error occurred")

    elif command_to_execute == "Delete":
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print("An error occurred")

    command = input()
