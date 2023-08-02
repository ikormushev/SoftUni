from math import ceil

gender = input()
weight_kg = float(input())
height_m = float(input())
age_years = int(input())
physical_activity_level = input()

physical_activity = {
    "sedentary": 1.2,
    "lightly active": 1.375,
    "moderately active": 1.55,
    "very active": 1.725
}

metabolism_base_level = 0

if gender == "m":
    metabolism_base_level = 66 + (13.7 * weight_kg) + (5 * (height_m * 100)) - (6.8 * age_years)
elif gender == "f":
    metabolism_base_level = 655 + (9.6 * weight_kg) + (1.8 * (height_m * 100)) - (4.7 * age_years)

metabolism_base_level *= physical_activity[physical_activity_level]

print(f"To maintain your current weight you will need"
      f" {ceil(metabolism_base_level)} calories per day.")
