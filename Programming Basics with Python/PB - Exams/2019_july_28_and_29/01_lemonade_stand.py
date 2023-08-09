lemons_kg = float(input())
sugar_kg = float(input())
water_lt = float(input())

lemon_juice_ml = lemons_kg * 980
mixture = lemon_juice_ml + water_lt * 1000 + (sugar_kg * 0.30)

lemonade_cups = mixture // 150
earnings = lemonade_cups * 1.20

print(f"All cups sold: {lemonade_cups}")
print(f"Money earned: {earnings:.2f}")
