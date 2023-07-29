hikers_num = int(input())
carabiners_num = int(input())  # per hiker
ropes_num = int(input())  # per hiker
axes_num = int(input())  # per hiker

VAT = 0.20
carabiners_price = carabiners_num * 36
ropes_price = ropes_num * 3.60
axes_price = axes_num * 19.80

price_per_hiker = carabiners_price + ropes_price + axes_price
total_price = price_per_hiker * hikers_num
total_price *= 1 + VAT

print(f"{total_price:.2f}")
