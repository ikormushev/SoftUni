holiday_days = int(input())

daily_limit = 0

for i in range(1, holiday_days + 1):
    daily_sum = 0
    products_bought = 0
    daily_limit += 60
    while True:
        command = input()
        if command == "Day over":
            money_left = daily_limit - daily_sum
            print(f"Money left from today: {money_left:.2f}. "
                  f"You've bought {products_bought} products.")
            break
        product_price = float(command)
        daily_limit -= product_price
        if daily_limit < 0:
            daily_limit += product_price
            continue
        products_bought += 1
        if daily_limit == 0:
            print(f"Daily limit exceeded! You've bought {products_bought} products.")
            break
