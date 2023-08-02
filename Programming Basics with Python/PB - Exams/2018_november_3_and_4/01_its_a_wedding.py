whiskey_price = float(input())
water_lt = float(input())
wine_lt = float(input())
champagne_lt = float(input())
whiskey_lt = float(input())

champagne_price = whiskey_price * 0.50
wine_price = champagne_price * 0.40
water_price = champagne_price * 0.10

whiskey = whiskey_lt * whiskey_price
water = water_lt * water_price
champagne = champagne_lt * champagne_price
wine = wine_lt * wine_price

total_price = whiskey + water + champagne + wine

print(f"{total_price:.2f}")
