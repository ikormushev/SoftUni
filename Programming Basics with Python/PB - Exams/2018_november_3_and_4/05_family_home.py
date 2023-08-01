months = int(input())

electricity, water, internet, other = 0, 0, 0, 0

for _ in range(1, months + 1):
    electricity_price = float(input())
    water += 20
    internet += 15
    electricity += electricity_price
    other += (electricity_price + 20 + 15) * 1.20

bill = electricity + water + internet + other
average_bill = bill / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average_bill:.2f} lv")
