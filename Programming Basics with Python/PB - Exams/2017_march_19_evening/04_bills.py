months = int(input())

electricity, water, internet, other = 0, 0, 0, 0

for _ in range(1, months + 1):
    electricity_price = float(input())
    other_price = (electricity_price + 20 + 15) * 1.20
    electricity += electricity_price
    water += 20
    internet += 15
    other += other_price

bills_average_price = (electricity + water + internet + other) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {bills_average_price:.2f} lv")
