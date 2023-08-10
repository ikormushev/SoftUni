budget = float(input())

total_price = 2.5
budget_left = budget
total_products = 0

while True:
    command = input()
    if command == "Order":
        print(f"You ordered {total_products} items!")
        print(f"Total: {total_price:.2f}")
        break
    product_name = command
    product_price = float(input())
    budget_left -= product_price
    if budget_left < 0:
        budget_left += product_price
        print("You will exceed the budget if you order this!")
        continue
    total_products += 1
    total_price += product_price
