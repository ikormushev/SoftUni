flower_type = input()
flowers_num = int(input())
season = input()

production = 0

honey_production_spring = {
    "Sunflower": 10,
    "Daisy": 12,
    "Lavender": 12,
    "Mint": 10
}

honey_production_summer = {
    "Sunflower": 8,
    "Daisy": 8,
    "Lavender": 8,
    "Mint": 12
}

honey_production_autumn = {
    "Sunflower": 12,
    "Daisy": 6,
    "Lavender": 6,
    "Mint": 6
}

if season == "Spring":
    if flower_type == "Daisy":
        honey_production_spring[flower_type] *= 1.10
    elif flower_type == "Mint":
        honey_production_spring[flower_type] *= 1.10
    production = flowers_num * honey_production_spring[flower_type]
elif season == "Summer":
    production = flowers_num * honey_production_summer[flower_type]
    production *= 1.10
elif season == "Autumn":
    production = flowers_num * honey_production_autumn[flower_type]
    production *= 0.95

print(f"Total honey harvested: {production:.2f}")
