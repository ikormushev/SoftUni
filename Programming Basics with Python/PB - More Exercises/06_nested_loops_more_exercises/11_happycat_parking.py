days = int(input())
hours = int(input())

total_sum = 0

for d in range(1, days + 1):
    daily_fee = 0
    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 == 1:
            daily_fee += 2.5
        elif d % 2 == 1 and h % 2 == 0:
            daily_fee += 1.25
        else:
            daily_fee += 1
    total_sum += daily_fee
    print(f"Day: {d} - {daily_fee:.2f} leva")

print(f"Total: {total_sum:.2f} leva")
