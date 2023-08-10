days = int(input())
hours = int(input())

total_parking = 0

for d in range(1, days + 1):
    daily_parking = 0
    for h in range(1, hours + 1):
        if (d % 2 == 0) and (h % 2 == 1):
            parking = 2.50
        elif (d % 2 == 1) and (h % 2 == 0):
            parking = 1.25
        else:
            parking = 1
        daily_parking += parking
    print(f"Day: {d} - {daily_parking:.2f} leva")
    total_parking += daily_parking

print(f"Total: {total_parking:.2f} leva")
