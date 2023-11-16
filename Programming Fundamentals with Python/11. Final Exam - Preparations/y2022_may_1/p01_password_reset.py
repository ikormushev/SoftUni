given_string = input()

while True:
    command = input()
    if command == "Done":
        print(f"Your password is: {given_string}")
        break

    if command == "TakeOdd":
        new_password = ""
        for i in range(0, len(given_string)):
            if i % 2 == 1:
                new_password += given_string[i]

        given_string = new_password
        print(given_string)

    action = command.split(" ")
    if action[0] == "Cut":
        index = int(action[1])
        length = int(action[2])
        removal = given_string[index:index+length]
        given_string = given_string.replace(removal, "", 1)
        print(given_string)
    elif action[0] == "Substitute":
        substring = action[1]
        substitute = action[2]
        if substring in given_string:
            given_string = given_string.replace(substring, substitute)
            print(given_string)
        else:
            print(f"Nothing to replace!")
