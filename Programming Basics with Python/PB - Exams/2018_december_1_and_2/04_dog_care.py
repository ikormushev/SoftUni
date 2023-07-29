purchased_food_kg = int(input())

purchased_food_gr = purchased_food_kg * 1000
total_food_eaten = 0

while True:
    food = input()
    if food == "Adopted":
        break
    else:
        food_eaten = int(food)
        total_food_eaten += food_eaten

food_diff = abs(purchased_food_gr - total_food_eaten)

if total_food_eaten <= purchased_food_gr:
    print(f"Food is enough! Leftovers: {food_diff} grams.")
else:
    print(f"Food is not enough. You need {food_diff} grams more.")
