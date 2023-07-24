from math import floor

cups_num = int(input())
workers_num = int(input())
workdays = int(input())

cups_price = cups_num * 4.20
work_hours = workers_num * workdays * 8

cups_made = floor(work_hours / 5)
cups_made_price = cups_made * 4.20

money_diff = abs(cups_price - cups_made_price)

if cups_made > cups_num:
    print(f"{money_diff:.2f} extra money")
elif cups_made < cups_num:
    print(f"Losses: {money_diff:.2f}")
