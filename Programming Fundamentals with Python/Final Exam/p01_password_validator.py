def password_validation(given_password):
    uppercase_letters_count = 0
    lowercase_letters_count = 0
    digits_count = 0
    other_symbol_found = False

    if len(given_password) < 8:
        print("Password must be at least 8 characters long!")

    for i in range(len(given_password)):
        if given_password[i].isalpha() or given_password[i].isnumeric() or given_password[i] == "_":
            if given_password[i].isupper():
                uppercase_letters_count += 1
            elif given_password[i].islower():
                lowercase_letters_count += 1
            elif given_password[i].isnumeric():
                digits_count += 1
        else:
            other_symbol_found = True

    if other_symbol_found:
        print("Password must consist only of letters, digits and _!")
    if uppercase_letters_count < 1:
        print("Password must consist at least one uppercase letter!")
    if lowercase_letters_count < 1:
        print("Password must consist at least one lowercase letter!")
    if digits_count < 1:
        print("Password must consist at least one digit!")


password = input()

while True:
    command = input()
    if command == "Complete":
        break

    password = list(password)
    if "Validation" == command:
        password_validation(password)

    action = command.split(" ")
    if "Make" == action[0]:
        if "Upper" == action[1]:
            index = int(action[2])
            password[index] = password[index].upper()
            print("".join(password))

        elif "Lower" == action[1]:
            index = int(action[2])
            password[index] = password[index].lower()
            print("".join(password))

    elif "Insert" == action[0]:
        index = int(action[1])
        character = action[2]
        password.insert(index, character)
        print("".join(password))

    elif "Replace" == action[0]:
        character = action[1]
        value = int(action[2])
        if character not in password:
            continue
        new_symbol = chr(ord(character) + value)
        password = "".join(password)
        password = password.replace(character, new_symbol)
        password = list(password)
        print("".join(password))
