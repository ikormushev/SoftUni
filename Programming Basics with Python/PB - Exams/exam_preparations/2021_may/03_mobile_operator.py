contract_length = input()
contract_type = input()
internet = input()
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

monthly_price = prices[contract_length][contract_type]

if internet == "yes":
    if monthly_price <= 10.00:
        monthly_price += 5.50
    elif monthly_price <= 30.00:
        monthly_price += 4.35
    else:
        monthly_price += 3.85

price = monthly_price * months
if contract_length == "two":
    price *= 0.9625

print(f"{price:.2f} lv.")
