budget = float(input())
fuel_needed_lt = float(input())
day = input()

discounts = {
    "Saturday": 0.10,
    "Sunday": 0.20
}

fuel_price = fuel_needed_lt * 2.10
total_price = fuel_price + 100
total_price *= 1 - discounts[day]
money_diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Safari time! Money left: {money_diff:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {money_diff:.2f} lv.")
