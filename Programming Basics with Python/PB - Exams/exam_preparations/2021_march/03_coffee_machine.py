drink = input()
sugar = input()
drinks_num = int(input())

prices = {
    "Without": {
        "Espresso": 0.90,
        "Cappuccino": 1.00,
        "Tea": 0.50
    },
    "Normal": {
        "Espresso": 1.00,
        "Cappuccino": 1.20,
        "Tea": 0.60
    },
    "Extra": {
        "Espresso": 1.20,
        "Cappuccino": 1.60,
        "Tea": 0.70
    }
}

price = prices[sugar][drink] * drinks_num

if sugar == "Without":
    price *= 0.65

if drink == "Espresso" and drinks_num >= 5:
    price *= 0.75

if price > 15:
    price *= 0.80

print(f"You bought {drinks_num} cups of {drink} for {price:.2f} lv.")
