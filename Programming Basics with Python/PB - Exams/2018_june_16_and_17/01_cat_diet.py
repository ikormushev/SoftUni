fats_percent = int(input()) / 100
protein_percent = int(input()) / 100
carbs_percent = int(input()) / 100
total_calories = int(input())
water_percent = int(input()) / 100

fats = (fats_percent * total_calories) / 9
protein = (protein_percent * total_calories) / 4
carbs = (carbs_percent * total_calories) / 4
food_gr = fats + protein + carbs

food_calories_per_gr = total_calories / food_gr
water_gr = water_percent * food_calories_per_gr
food_calories_per_gr -= water_gr

print(f"{food_calories_per_gr:.4f}")
