budget = int(input())
phones_num = int(input())
phone_brand = input()

phone_brands_prices = {
    "Gsm4e": 20.50,
    "Mobifon4e": 50.75,
    "Telefon4e": 115
}

phone_brands_discounts = {
    "Gsm4e": 0.01,
    "Mobifon4e": 0.02,
    "Telefon4e": 0.03
}

price = phone_brands_prices[phone_brand] * phones_num

if phones_num <= 10:
    price *= 1 - phone_brands_discounts[phone_brand]
if 10 < phones_num <= 20:
    price *= (0.98 - phone_brands_discounts[phone_brand])
elif 20 < phones_num <= 50:
    price *= (0.95 - phone_brands_discounts[phone_brand])
elif phones_num > 50:
    price *= (0.93 - phone_brands_discounts[phone_brand])

money_diff = abs(budget - price)
if budget > price:
    print(f"The company bought all mobile phones. "
          f"{money_diff:.2f} leva left.")
elif budget < price:
    print(f"Not enough money for all mobiles. "
          f"Company needs {money_diff:.2f} more leva.")
