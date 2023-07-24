photos_num = int(input())
photos_type = input()
order_type = input()

price = 0
discount = 0

if photos_type == "9X13":
    price = photos_num * 0.16
    if photos_num >= 50:
        price *= 0.95
elif photos_type == "10X15":
    price = photos_num * 0.16
    if photos_num >= 80:
        price *= 0.97
elif photos_type == "13X18":
    price = photos_num * 0.38
    if 50 <= photos_num <= 100:
        price *= 0.97
    elif photos_num > 100:
        price += 0.95
elif photos_type == "20X30":
    price = photos_num * 2.90
    if 10 <= photos_num <= 50:
        price *= 0.93
    elif photos_num > 50:
        price *= 0.91

if order_type == "online":
    discount = price * 0.02
    price -= discount

print(f"{price:.2f}BGN")
