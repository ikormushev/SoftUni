starting_eggs = int(input())

eggs_left = starting_eggs
eggs_sold = 0

while True:
    command = input()
    if command == "Close":
        print("Store is closed!")
        print(f"{eggs_sold} eggs sold.")
        break

    new_command = command
    eggs = int(input())

    if new_command == "Buy":
        eggs_left -= eggs
        if eggs_left < 0:
            eggs_left += eggs
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_left}.")
            break
        eggs_sold += eggs
    elif new_command == "Fill":
        eggs_left += eggs
