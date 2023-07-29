from math import ceil

days_away = int(input())
starting_food = int(input())
first_dog_food = float(input())
second_dog_food = float(input())
third_dog_food = float(input())

total_food_first_dog = first_dog_food * days_away
total_food_second_dog = second_dog_food * days_away
total_food_third_dog = third_dog_food * days_away

total_food = total_food_first_dog + total_food_second_dog + total_food_third_dog

food_diff = abs(starting_food - total_food)

if starting_food >= total_food:
    print(f"{food_diff:.0f} kilos of food left.")
else:
    print(f"{ceil(food_diff)} more kilos of food are needed.")
