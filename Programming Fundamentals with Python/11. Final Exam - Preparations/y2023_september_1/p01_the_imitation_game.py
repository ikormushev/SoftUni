encrypted_message = list(input())

while True:
    command = input()
    if command == "Decode":
        print(f"The decrypted message is: {''.join(map(str,encrypted_message))}")
        break
    decode_command = command.split("|")
    action = decode_command[0]
    if action == "Move":
        letters_to_move_num = int(decode_command[1])
        if letters_to_move_num < 0 or letters_to_move_num > len(encrypted_message):
            continue
        letters_to_move = encrypted_message[:letters_to_move_num]
        if letters_to_move_num != 0:
            encrypted_message += letters_to_move
            for _ in range(letters_to_move_num):
                encrypted_message.pop(0)

    elif action == "Insert":
        index = int(decode_command[1])
        value = list(decode_command[2])
        if 0 <= index <= len(encrypted_message):
            first_half = encrypted_message[:index]
            second_half = encrypted_message[index:]
            encrypted_message = first_half + value + second_half

    elif action == "ChangeAll":
        substring = decode_command[1]
        replacement = decode_command[2]

        for i in range(len(encrypted_message)):
            if encrypted_message[i] == substring:
                encrypted_message[i] = replacement
