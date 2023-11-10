concealed_message = list(input())

while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {''.join(concealed_message)}")
        break
    action = command.split(":|:")

    if action[0] == "InsertSpace":
        index = int(action[1])
        concealed_message.insert(index, " ")

    elif action[0] == "Reverse":
        substring = action[1]
        joined_message = "".join(concealed_message)
        if substring in joined_message:
            joined_message = joined_message.replace(substring, "", 1)
            concealed_message = list(joined_message)
            new_substring = list(substring[::-1])
            concealed_message += new_substring
        else:
            print("error")
            continue

    elif action[0] == "ChangeAll":
        substring = action[1]
        replacement = action[2]
        joined_message = "".join(concealed_message)
        joined_message = joined_message.replace(substring, replacement)
        concealed_message = list(joined_message)

    print("".join(concealed_message))
