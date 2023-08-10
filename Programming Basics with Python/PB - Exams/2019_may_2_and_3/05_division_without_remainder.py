total_numbers = int(input())

p1, p2, p3 = 0, 0, 0

for _ in range(1, total_numbers + 1):
    new_number = int(input())
    if new_number % 2 == 0:
        p1 += 1
    if new_number % 3 == 0:
        p2 += 1
    if new_number % 4 == 0:
        p3 += 1

p1_percentage = p1 / total_numbers * 100
p2_percentage = p2 / total_numbers * 100
p3_percentage = p3 / total_numbers * 100

print(f"{p1_percentage:.2f}%")
print(f"{p2_percentage:.2f}%")
print(f"{p3_percentage:.2f}%")
