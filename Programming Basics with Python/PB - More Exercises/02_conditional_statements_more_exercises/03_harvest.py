from math import ceil, floor

vineyard_area = int(input())
grapes_kg_per_m = float(input())
needed_wine_lt = int(input())
workers = int(input())

total_grapes = vineyard_area * grapes_kg_per_m
wine_production_area = total_grapes * 0.4
wine_lt = wine_production_area / 2.5

wine_difference = abs(wine_lt - needed_wine_lt)

if wine_lt < needed_wine_lt:
    wine_difference = floor(wine_difference)
    print(f"It will be a tough winter! More {wine_difference} liters wine needed.")
else:
    wine_lt = floor(wine_lt)
    wine_per_worker = wine_difference / workers
    rounded_wine_per_worker = ceil(wine_difference / workers)
    wine_difference = ceil(wine_difference)
    print(f"Good harvest this year! Total wine: {wine_lt} liters.")
    print(f"{wine_difference} liters left -> {rounded_wine_per_worker} liters per person.")
