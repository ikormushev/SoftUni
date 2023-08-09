number = int(input())

division_num = 0

for n in range(1111, 10000):
    special_number = str(n)
    division_num = 0
    for i in range(len(special_number)):
        if int(special_number[i]) == 0:
            break
        if number % int(special_number[i]) == 0:
            division_num += 1
            continue
        else:
            break
    if division_num == 4:
        print(f"{special_number}", end=" ")
