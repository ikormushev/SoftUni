months = int(input())

electricity, water, internet, other = 0, 0, 0, 0  # bills
water_price, internet_price = 20, 15

for _ in range(1, months + 1):
    electricity_price = float(input())
    electricity += electricity_price
    water += water_price
    internet += internet_price
    other += (electricity_price + water_price + internet_price) * 1.20

total_bill = electricity + water + internet + other
monthly_average = total_bill / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {monthly_average:.2f} lv")
