stadium_capacity = int(input())
fans_num = int(input())

s1, s2, s3, s4 = 0, 0, 0, 0  # sectors_numbers
fans = 0

for _ in range(fans_num):
    sector = input()
    fans += 1
    if sector == "A":
        s1 += 1
    elif sector == "B":
        s2 += 1
    elif sector == "V":
        s3 += 1
    elif sector == "G":
        s4 += 1

s1_percent = s1 / fans * 100
s2_percent = s2 / fans * 100
s3_percent = s3 / fans * 100
s4_percent = s4 / fans * 100

fans_percent = fans / stadium_capacity * 100

print(f"{s1_percent:.2f}%")
print(f"{s2_percent:.2f}%")
print(f"{s3_percent:.2f}%")
print(f"{s4_percent:.2f}%")
print(f"{fans_percent:.2f}%")
