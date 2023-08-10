from math import ceil

budget = float(input())
floor_width = float(input())
floor_length = float(input())
triangle_side = float(input())
triangle_height = float(input())
tile_price = float(input())
repairer_price = float(input())

floor_area = floor_width * floor_length
triangle_area = triangle_side * triangle_height
tile_area = triangle_area / 2

tiles_needed = ceil(floor_area / tile_area) + 5
tiles_price = tiles_needed * tile_price

total_price = tiles_price + repairer_price
money_diff = abs(budget - total_price)

if budget >= total_price:
    print(f"{money_diff:.2f} lv left.")
else:
    print(f"You'll need {money_diff:.2f} lv more.")
