food_purchased_kg = int(input())

food_left = food_purchased_kg * 1000

while True:
    command = input()
    if command == "Adopted":
        break
    food_eaten = int(command)
    food_left -= food_eaten

if food_left >= 0:
    print(f"Food is enough! Leftovers: {food_left} grams.")
else:
    print(f"Food is not enough. You need {abs(food_left)} grams more.")
