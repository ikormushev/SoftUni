inheritance = float(input())
year_to_live = int(input())

age = 17
money_needed = 0

for i in range(1800, year_to_live + 1):
    age += 1
    if i % 2 == 0:
        money_needed += 12000
    else:
        money_needed += 12000 + (50 * age)

money_diff = abs(inheritance - money_needed)

if inheritance >= money_needed:
    print(f"Yes! He will live a carefree life "
          f"and will have {money_diff:.2f} dollars left.")
else:
    print(f"He will need {money_diff:.2f} dollars to survive.")
