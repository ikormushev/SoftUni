contract_length = input()
contract_type = input()
dessert = input()
months = int(input())

prices = {
    "one": {
        "Small": 9.98,
        "Middle": 18.99,
        "Large": 25.98,
        "ExtraLarge": 35.99
    },
    "two": {
        "Small": 8.58,
        "Middle": 17.09,
        "Large": 23.59,
        "ExtraLarge": 31.79
    }
}

price_total = prices[contract_length][contract_type]

if dessert == "yes":
    if price_total <= 10:
        price_total += 5.50
    elif price_total <= 30:
        price_total += 4.35
    elif price_total > 30:
        price_total += 3.85

if contract_length == "two":
    price_total *= 0.9625

price_total *= months
print(f"{price_total:.2f} lv.")
