days = int(input())

total_degrees = 0
total_rakia_lt = 0

for d in range(1, days + 1):
    rakia_amount = float(input())
    rakia_degrees = float(input())

    total_rakia_lt += rakia_amount
    total_degrees += rakia_amount * rakia_degrees

average_degrees = total_degrees / total_rakia_lt

print(f"Liter: {total_rakia_lt:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
