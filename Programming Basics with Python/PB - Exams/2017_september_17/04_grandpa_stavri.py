days = int(input())

rakia_lt_total = 0
degrees_total = 0

for _ in range(1, days + 1):
    rakia_lt = float(input())
    rakia_degrees = float(input())
    rakia_lt_total += rakia_lt
    degrees = rakia_lt * rakia_degrees
    degrees_total += degrees

degrees_total = degrees_total / rakia_lt_total
print(f"Liter: {rakia_lt_total:.2f}")
print(f"Degrees: {degrees_total:.2f}")

if degrees_total < 38:
    print("Not good, you should baking!")
elif 38 <= degrees_total <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
