floors_num = int(input())
apartments_total = int(input())

room_letter = ""

for floor in range(floors_num, 0, -1):
    if floor == floors_num or floors_num == 1:
        room_letter = "L"
    elif floor % 2 == 0:
        room_letter = "O"
    else:
       room_letter = "A"
    for room in range(apartments_total):
        print(f"{room_letter}{floor}{room}", end=" ")
    print()
