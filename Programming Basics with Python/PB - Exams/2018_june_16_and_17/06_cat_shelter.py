food_purchased_kg = int(input())

food_left_gr = food_purchased_kg * 1000

while True:
    command = input()
    if command == "Adopted":
        break
    food_eaten_gr = int(command)
    food_left_gr -= food_eaten_gr

if food_left_gr >= 0:
    print(f"Food is enough! Leftovers: {food_left_gr} grams.")
else:
    print(f"Food is not enough. You need {abs(food_left_gr)} grams more.")
