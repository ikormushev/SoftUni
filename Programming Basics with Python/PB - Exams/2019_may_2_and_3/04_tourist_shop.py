budget = float(input())

budget_left = budget
total_price = 0
items_count = 0

while True:
    command = input()
    if command == "Stop":
        print(f"You bought {items_count} products for {total_price:.2f} leva.")
        break
    item_name = command
    item_price = float(input())
    items_count += 1
    if items_count % 3 == 0:
        item_price *= 1/2
    budget_left -= item_price
    total_price += item_price
    if budget_left < 0:
        print("You don't have enough money!")
        print(f"You need {abs(budget_left):.2f} leva!")
        break
