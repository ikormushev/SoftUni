from math import ceil

people_num = int(input())
entry_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

umbrellas_num = ceil(people_num / 2)
sunbeds_num = ceil(people_num * 0.75)

entry_fees = entry_fee * people_num
sunbeds = sunbeds_num * sunbed_price
umbrellas = entry_fees + umbrellas_num * umbrella_price

total_price = sunbeds + umbrellas

print(f"{total_price:.2f} lv.")
