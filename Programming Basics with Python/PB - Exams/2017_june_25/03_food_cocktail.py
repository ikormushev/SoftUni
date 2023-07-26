fruit = input()
cocktail_size = input()
cocktails_num = int(input())

small_cocktails_prices_lt = {
    "Watermelon": 56,
    "Mango": 36.66,
    "Pineapple": 42.10,
    "Raspberry": 20
}

big_cocktails_prices_lt = {
    "Watermelon": 28.70,
    "Mango": 19.60,
    "Pineapple": 24.80,
    "Raspberry": 15.20
}

price = 0

if cocktail_size == "small":
    price = small_cocktails_prices_lt[fruit] * 2
elif cocktail_size == "big":
    price = big_cocktails_prices_lt[fruit] * 5

price *= cocktails_num

if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.5

print(f"{price:.2f} lv.")
