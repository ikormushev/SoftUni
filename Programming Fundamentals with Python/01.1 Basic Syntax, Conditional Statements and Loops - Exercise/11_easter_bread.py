budget = float(input())
flour_kg_price = float(input())

eggs_pack_price = flour_kg_price * 0.75
milk_lt_price = flour_kg_price * 1.25

budge_left = budget
loaves_num = 0
colored_eggs_num = 0

while True:
    loaf_price = eggs_pack_price + flour_kg_price + (milk_lt_price * 0.250)
    budge_left -= loaf_price

    if budge_left < 0:
        budge_left += loaf_price
        break

    colored_eggs_num += 3
    loaves_num += 1
    if loaves_num % 3 == 0:
        colored_eggs_num -= loaves_num - 2

print(f"You made {loaves_num} loaves of Easter bread! "
      f"Now you have {colored_eggs_num} eggs "
      f"and {budge_left:.2f}BGN left.")
