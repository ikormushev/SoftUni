from math import ceil, floor

days_num = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

dog_food = days_num * dog_food_kg
cat_food = days_num * cat_food_kg
turtle_food = days_num * (turtle_food_gr / 1000)

total_food = dog_food + cat_food + turtle_food

food_difference = abs(total_food - food_kg)
if total_food <= food_kg:
    food_difference = floor(food_difference)
    print(f"{food_difference} kilos of food left.")
else:
    food_difference = ceil(food_difference)
    print(f"{food_difference} more kilos of food are needed.")
