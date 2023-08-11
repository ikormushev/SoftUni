from math import ceil

guests_num = int(input())
budget = int(input())

bread_num = ceil(guests_num / 3)
bakes_price = bread_num * 4
eggs_num = guests_num * 2
eggs_price = eggs_num * 0.45

total_price = bakes_price + eggs_price

money_diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Lyubo bought {bread_num} Easter bread and {eggs_num} eggs.")
    print(f"He has {money_diff:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {money_diff:.2f} lv. more.")
