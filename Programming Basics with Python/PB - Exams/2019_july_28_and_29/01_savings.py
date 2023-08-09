salary = float(input())
months = int(input())
money_needed_personal = float(input())

unexpected_spending = salary * 0.30
monthly_savings = salary - unexpected_spending - money_needed_personal
total_savings = monthly_savings * months

savings_percentage = monthly_savings / salary * 100

print(f"She can save {savings_percentage:.2f}%")
print(f"{total_savings:.2f}")
