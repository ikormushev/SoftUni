contacts_searched_num = 0
contacts = {}

while True:
    command = input()
    if command.isnumeric():
        contacts_searched_num = int(command)
        break
    phonebook = command.split("-")
    name = phonebook[0]
    phone = phonebook[1]
    contacts[name] = phone

for _ in range(contacts_searched_num):
    wanted_name = input()
    if wanted_name in contacts:
        print(f"{wanted_name} -> {contacts[wanted_name]}")
    else:
        print(f"Contact {wanted_name} does not exist.")
