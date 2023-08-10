budget = float(input())
needed_gas_lt = float(input())
day = input()

gas_price = needed_gas_lt * 2.10
price = gas_price + 100

if day == "Saturday":
    price *= 0.90
elif day == "Sunday":
    price *= 0.80

money_diff = abs(budget - price)

if budget >= price:
    print(f"Safari time! Money left: {money_diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {money_diff:.2f} lv.")
