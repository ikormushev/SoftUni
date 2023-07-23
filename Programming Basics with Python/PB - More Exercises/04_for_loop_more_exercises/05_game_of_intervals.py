turns_num = int(input())

i1, i2, i3, i4, i5 = 0, 0, 0, 0, 0  # intervals
invalid_numbers = 0
total_numbers = 0
points = 0

for _ in range(turns_num):
    new_number = int(input())
    if 0 <= new_number <= 9:
        points += new_number * 0.20
        i1 += 1
    elif 10 <= new_number <= 19:
        points += new_number * 0.30
        i2 += 1
    elif 20 <= new_number <= 29:
        points += new_number * 0.40
        i3 += 1
    elif 30 <= new_number <= 39:
        points += 50
        i4 += 1
    elif 40 <= new_number <= 50:
        points += 100
        i5 += 1
    else:
        points = points / 2
        invalid_numbers += 1
    total_numbers += new_number

i1_percent = i1 / turns_num * 100
i2_percent = i2 / turns_num * 100
i3_percent = i3 / turns_num * 100
i4_percent = i4 / turns_num * 100
i5_percent = i5 / turns_num * 100
invalid_numbers_percent = invalid_numbers / turns_num * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {i1_percent:.2f}%")
print(f"From 10 to 19: {i2_percent:.2f}%")
print(f"From 20 to 29: {i3_percent:.2f}%")
print(f"From 30 to 39: {i4_percent:.2f}%")
print(f"From 40 to 50: {i5_percent:.2f}%")
print(f"Invalid numbers: {invalid_numbers_percent:.2f}%")
