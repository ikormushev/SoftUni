budget = float(input())

budget_left = budget
products_num = 0
total_price = 0

while True:
    command = input()
    if command == "Stop":
        print(f"You bought {products_num} products for {total_price:.2f} leva.")
        break
    product_name = command
    product_price = float(input())
    products_num += 1

    if products_num % 3 == 0:
        product_price *= 0.50

    total_price += product_price
    budget_left -= product_price

    if budget_left < 0:
        print("You don't have enough money!")
        print(f"You need {abs(budget_left):.2f} leva!")
        break
