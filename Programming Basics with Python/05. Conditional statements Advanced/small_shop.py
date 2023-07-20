product = input()
city = input()
amount = float(input())

price = 0

if product == "coffee":
    if city == "Sofia":
        price = 0.50 * amount
    elif city == "Plovdiv":
        price = 0.40 * amount
    elif city == "Varna":
        price = 0.45 * amount
elif product == "water":
    if city == "Sofia":
        price = 0.80 * amount
    elif city == "Plovdiv":
        price = 0.70 * amount
    elif city == "Varna":
        price = 0.70 * amount
elif product == "beer":
    if city == "Sofia":
        price = 1.20 * amount
    elif city == "Plovdiv":
        price = 1.15 * amount
    elif city == "Varna":
        price = 1.10 * amount
elif product == "sweets":
    if city == "Sofia":
        price = 1.45 * amount
    elif city == "Plovdiv":
        price = 1.30 * amount
    elif city == "Varna":
        price = 1.35 * amount
elif product == "peanuts":
    if city == "Sofia":
        price = 1.60 * amount
    elif city == "Plovdiv":
        price = 1.50 * amount
    elif city == "Varna":
        price = 1.55 * amount

print(price)
