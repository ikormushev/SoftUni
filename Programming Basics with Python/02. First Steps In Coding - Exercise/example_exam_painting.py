nylon_square_m = int(input())
paint_lt = int(input())
diluent_lt = int(input())
hours_workers = int(input())

price_nylon = (nylon_square_m + 2) * 1.5
price_color = (paint_lt + 0.1 * paint_lt) * 14.5
price_diluent = diluent_lt * 5
price_bags = 0.4

price_materials = price_nylon + price_color + price_diluent + price_bags

price_for_work = (price_materials * 0.3) * hours_workers

final_price = price_materials + price_for_work

print(final_price)
