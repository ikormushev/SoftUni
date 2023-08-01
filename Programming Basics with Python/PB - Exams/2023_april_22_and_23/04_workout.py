from math import ceil

days = int(input())
first_day_km = float(input())

day_norm_km = first_day_km
km_total = first_day_km

for _ in range(1, days + 1):
    percentage_increase = int(input()) / 100
    day_norm_km *= 1 + percentage_increase
    km_total += day_norm_km

km_diff = abs(1000 - km_total)

if km_total < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(km_diff)} more kilometers")
else:
    print(f"You've done a great job running {ceil(km_diff)} more kilometers!")
