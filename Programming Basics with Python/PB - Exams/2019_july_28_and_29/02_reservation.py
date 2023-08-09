day_created_res = int(input())
month_created_res = int(input())
day_res = int(input())
month_res = int(input())
day_leaving = int(input())
month_leaving = int(input())

night_price = 30
discount = 0

if (abs(day_created_res - day_res)) >= 10:
    night_price = 25

if (month_created_res - month_res) < 0:
    night_price = 25
    discount = 0.20

nights = day_leaving - day_res
price = (nights * night_price) * (1 - discount)

print(f"Your stay from {day_res}/{month_res} to "
      f"{day_leaving}/{month_leaving} will cost {price:.2f}")
