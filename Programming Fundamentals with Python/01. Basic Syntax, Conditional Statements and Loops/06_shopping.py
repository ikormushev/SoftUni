budget = int(input())

budget_left = budget

while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break
    product_price = int(command)
    budget_left -= product_price

    if budget_left < 0:
        print("You went in overdraft!")
        break
