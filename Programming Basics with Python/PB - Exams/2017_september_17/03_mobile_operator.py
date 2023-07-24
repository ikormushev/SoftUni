contract_duration = input()
contract_type = input()
internet = input()
months_num = int(input())

price = 0
internet_price = 0
contract_types = ["Small", "Middle", "Large", "ExtraLarge"]

one_year_contract_prices = {
    "Small": 9.98,
    "Middle": 18.99,
    "Large": 25.98,
    "ExtraLarge": 35.99
}

two_year_contract_prices = {
    "Small": 8.58,
    "Middle": 17.09,
    "Large": 23.59,
    "ExtraLarge": 31.79
}

if contract_type in contract_types:
    if contract_duration == "one":
        price = one_year_contract_prices[contract_type]
    elif contract_duration == "two":
        price = two_year_contract_prices[contract_type]

if internet == "yes":
    if price <= 10.00:
        internet_price = 5.50
    elif price <= 30.00:
        internet_price = 4.35
    elif price > 30.00:
        internet_price = 3.85

price += internet_price
price *= months_num

if contract_duration == "two":
    price *= 0.9625

print(f"{price:.2f} lv.")
