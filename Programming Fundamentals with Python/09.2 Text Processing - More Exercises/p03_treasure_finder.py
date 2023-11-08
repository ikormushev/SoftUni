import re

given_key = input().split(" ")

while True:
    command = input()
    if command == "find":
        break
    secret_message = list(command)
    number_from_key = 0
    for i in range(len(secret_message)):
        if number_from_key >= len(given_key):
            number_from_key = 0
        secret_message[i] = chr(ord(secret_message[i]) - int(given_key[number_from_key]))
        number_from_key += 1

    decrypted_message = "".join(secret_message)

    treasure_type_pattern = r"\&[a-zA-Z]+\&"
    treasure_coordinates_pattern = r"<\w+>"
    treasure_type = re.findall(treasure_type_pattern, decrypted_message)[0][1:-1]
    treasure_coordinates = re.findall(treasure_coordinates_pattern, decrypted_message)[0][1:-1]
    print(f"Found {treasure_type} at {treasure_coordinates}")
