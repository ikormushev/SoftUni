fats_percentage = int(input()) / 100
protein_percentage = int(input()) / 100
carbs_percentage = int(input()) / 100
calories = int(input())
water_percentage = int(input()) / 100

fats = (fats_percentage * calories) / 9
protein = (protein_percentage * calories) / 4
carbs = (carbs_percentage * calories) / 4

food_gr = fats + protein + carbs
calories_per_gr_food = calories / food_gr

water = calories_per_gr_food * water_percentage
actual_food = calories_per_gr_food - water

print(f"{actual_food:.4f}")
