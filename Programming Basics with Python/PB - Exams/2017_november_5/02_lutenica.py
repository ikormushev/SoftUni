from math import floor

tomatoes_kg = float(input())
baskets_num = int(input())
jars_num_per_basket = int(input())

lutenica_kg = tomatoes_kg / 5
lutenica_jars = lutenica_kg / 0.535
possible_baskets_num = lutenica_jars / jars_num_per_basket
jars_num = baskets_num * jars_num_per_basket

baskets_left = abs(baskets_num - possible_baskets_num)
jars_left = abs(jars_num - lutenica_jars)

print(f"Total lutenica: {floor(lutenica_kg)}")

if possible_baskets_num > baskets_num:
    print(f"{floor(baskets_left)} boxes left.")
    print(f"{floor(jars_left)} jars left.")
elif possible_baskets_num < baskets_num:
    print(f"{floor(baskets_left)} more boxes needed.")
    print(f"{floor(jars_left)} more jars needed.")
