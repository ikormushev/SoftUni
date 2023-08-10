budget = int(input())

budget_left = budget

while True:
    command = input()
    if command == "Stop":
        print(f"Money left: {budget_left}")
        break
    total_price = 0
    item_name = command
    for i in range(len(item_name)):
        letter_price = ord(item_name[i])
        total_price += letter_price
    budget_left -= total_price
    if budget_left < 0:
        print("Not enough money!")
        break
    else:
        print("Item successfully purchased!")
