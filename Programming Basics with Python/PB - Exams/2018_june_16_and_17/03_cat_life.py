cat_breed = input()
cat_gender = input()

cat_breeds = ["British Shorthair", "Siamese", "Persian",
              "Ragdoll", "American Shorthair", "Siberian"]

cat_life_expectancy_years = {
    "m": {
        "British Shorthair": 13,
        "Siamese": 15,
        "Persian": 14,
        "Ragdoll": 16,
        "American Shorthair": 12,
        "Siberian": 11
    },
    "f": {
        "British Shorthair": 14,
        "Siamese": 16,
        "Persian": 15,
        "Ragdoll": 17,
        "American Shorthair": 13,
        "Siberian": 12
    }
}

if cat_breed not in cat_breeds:
    print(f"{cat_breed} is invalid cat!")
else:
    cat_life_human_months = cat_life_expectancy_years[cat_gender][cat_breed] * 12
    cat_life_cat_months = cat_life_human_months // 6
    print(f"{cat_life_cat_months} cat months")
