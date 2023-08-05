floors_num = int(input())
apartments_total = int(input())

office_num = 0
apartment_num = 0

for floor in range(floors_num, 0, -1):
    if floor == floors_num or floors_num == 1:
        for i in range(apartments_total):
            if i == apartments_total - 1:
                print(f"L{floor}{apartment_num}", end="")
            else:
                print(f"L{floor}{apartment_num} ", end="")
            apartment_num += 1
        apartment_num = 0
    elif floor % 2 == 0:
        for i in range(apartments_total):
            if i == apartments_total - 1:
                print(f"O{floor}{office_num}", end="")
            else:
                print(f"O{floor}{office_num} ", end="")
            office_num += 1
        office_num = 0
    else:
        for i in range(apartments_total):
            if i == apartments_total - 1:
                print(f"A{floor}{apartment_num}", end="")
            else:
                print(f"A{floor}{apartment_num} ", end="")
            apartment_num += 1
        apartment_num = 0
    print()
