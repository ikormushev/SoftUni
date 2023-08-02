cats_num = int(input())

small, big, huge = 0, 0, 0  # cat_groups
total_food_gr = 0

for _ in range(1, cats_num + 1):
    food_gr = float(input())
    if 100 <= food_gr < 200:
        small += 1
    elif 200 <= food_gr < 300:
        big += 1
    elif 300 <= food_gr < 400:
        huge += 1
    total_food_gr += food_gr

total_food_kg = total_food_gr / 1000
total_food_price = total_food_kg * 12.45

print(f"Group 1: {small} cats.")
print(f"Group 2: {big} cats.")
print(f"Group 3: {huge} cats.")
print(f"Price for food per day: {total_food_price:.2f} lv.")
