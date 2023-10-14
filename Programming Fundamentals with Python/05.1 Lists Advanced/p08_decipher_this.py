def secret_code(letter: str) -> bool:
    if letter.isnumeric():
        return True
    return False


secret_message = input().split(" ")
deciphered_message = []

for i in range(len(secret_message)):
    temporary_message = list(secret_message[i])
    code = []
    for y in range(len(temporary_message)):
        if secret_code(temporary_message[y]):
            code.append(temporary_message[y])
            temporary_message[y] = ""

    new_letter = chr(int("".join(code)))
    for z in range(temporary_message.count("")):
        temporary_message.remove("")

    temporary_message.insert(0, new_letter)
    temporary_message[1], temporary_message[-1] = temporary_message[-1], temporary_message[1]
    deciphered_message.append("".join(temporary_message))


for k in range(len(deciphered_message)):
    print(deciphered_message[k], end=" ")
