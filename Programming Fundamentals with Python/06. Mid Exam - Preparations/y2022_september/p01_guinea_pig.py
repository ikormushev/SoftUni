food_quantity = float(input()) * 1000
hay_quantity = float(input()) * 1000
cover_quantity = float(input()) * 1000
pig_weight = float(input()) * 1000

days_in_month = 30

food_left = food_quantity
hay_left = hay_quantity
cover_left = cover_quantity

for i in range(1, days_in_month + 1):
    if food_left <= 0 or hay_left <= 0 or cover_left <= 0:
        break

    food_left -= 300
    if i % 2 == 0:
        hay_left -= food_left * 0.05
    if i % 3 == 0:
        cover_left -= pig_weight * 1/3

if food_left > 0 and hay_left > 0 and cover_left > 0:
    print(f"Everything is fine! Puppy is happy! "
          f"Food: {food_left / 1000:.2f}, "
          f"Hay: {hay_left / 1000:.2f}, "
          f"Cover: {cover_left / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")
