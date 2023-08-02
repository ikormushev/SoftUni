pastry = input()
pastries_num = int(input())
day_in_december = int(input())

pastries_prices_to_15 = {
    "Cake": 24,
    "Souffle": 6.66,
    "Baklava": 12.60
}

pastries_prices_after_15 = {
    "Cake": 28.70,
    "Souffle": 9.80,
    "Baklava": 16.98
}

price = 0

if day_in_december <= 15:
    price = pastries_prices_to_15[pastry] * pastries_num
elif day_in_december > 15:
    price = pastries_prices_after_15[pastry] * pastries_num

if day_in_december <= 22:
    if 100 <= price <= 200:
        price *= 0.85
    elif price > 200:
        price *= 0.75
    if day_in_december <= 15:
        price *= 0.90

print(f"{price:.2f}")
