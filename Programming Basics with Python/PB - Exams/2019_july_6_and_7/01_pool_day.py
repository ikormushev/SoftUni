from math import ceil

people_num = int(input())
entry_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

fees = people_num * entry_fee

sunbeds_num = ceil(people_num * 0.75)
sunbeds = sunbeds_num * sunbed_price

umbrellas_num = ceil(people_num * 0.50)
umbrellas = umbrellas_num * umbrella_price

final_price = fees + sunbeds + umbrellas

print(f"{final_price:.2f} lv.")
