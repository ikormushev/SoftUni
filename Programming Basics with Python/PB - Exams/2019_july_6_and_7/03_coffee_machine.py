coffee = input()
sugar = input()
coffees_num = int(input())

coffee_sugar_prices = {
    "Without": {
        "Espresso": 0.90,
        "Cappuccino": 1.00,
        "Tea": 0.50
    },
    "Normal": {
        "Espresso": 1,
        "Cappuccino": 1.20,
        "Tea": 0.60
    },
    "Extra": {
        "Espresso": 1.20,
        "Cappuccino": 1.60,
        "Tea": 0.70
    },
}

price = coffee_sugar_prices[sugar][coffee] * coffees_num

if sugar == "Without":
    price *= 0.65
if coffee == "Espresso" and coffees_num >= 5:
    price *= 0.75
if price > 15:  # it shouldn't be >= 15 even though it is shown in the instructions
    price *= 0.80

print(f"You bought {coffees_num} cups of {coffee} for {price:.2f} lv.")
