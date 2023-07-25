vineyard_area = float(input())
kg_per_sq_m = float(input())
waste_kg = float(input())

grapes_kg = vineyard_area * kg_per_sq_m
grapes_kg -= waste_kg

grapes_for_rakia = grapes_kg * 0.45
grapes_for_sale = grapes_kg * 0.55

rakia_lt = grapes_for_rakia / 7.50

rakia_price = rakia_lt * 9.80
grapes_price = grapes_for_sale * 1.50

print(f"{rakia_price:.2f}")
print(f"{grapes_price:.2f}")
