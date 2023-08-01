from math import ceil

fan_name = input()
budget = float(input())
beer_num = int(input())
chips_num = int(input())

beer = beer_num * 1.20
chips = ceil(chips_num * (beer * 0.45))

final_price = beer + chips
money_diff = abs(budget - final_price)

if budget >= final_price:
    print(f"{fan_name} bought a snack and has {money_diff:.2f} leva left.")
else:
    print(f"{fan_name} needs {money_diff:.2f} more leva!")
