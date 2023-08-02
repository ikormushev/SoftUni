cat_bed_price = float(input())
cat_toilet_monthly_price = float(input())

cat_food_monthly = 1.25 * cat_toilet_monthly_price
cat_toys_monthly = cat_food_monthly * 0.50
vet_visit_monthly = cat_toys_monthly * 1.10
monthly_expenses = cat_toilet_monthly_price + cat_food_monthly + \
                   cat_toys_monthly + vet_visit_monthly
unexpected_monthly_expenses = monthly_expenses * 0.05

first_year_expenses = cat_bed_price + (monthly_expenses + unexpected_monthly_expenses) * 12

print(f"{first_year_expenses:.2f} lv.")
