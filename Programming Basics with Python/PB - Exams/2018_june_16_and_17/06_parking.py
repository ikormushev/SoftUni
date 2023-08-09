days = int(input())
hours = int(input())

fee = 0
total_fee = 0

for d in range(1, days + 1):
    daily_fee = 0
    for h in range(1, hours + 1):
        if (d % 2 == 0) and (h % 2 == 1):
            fee = 2.50
        elif (d % 2 == 1) and (h % 2 == 0):
            fee = 1.25
        else:
            fee = 1
        daily_fee += fee
    total_fee += daily_fee
    print(f"Day: {d} - {daily_fee:.2f} leva")

print(f"Total: {total_fee:.2f} leva")
