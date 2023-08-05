interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

is_combination = False
combination_num = 0
x1 = 0
x2 = 0

for a in range(interval_start, interval_end + 1):
    if is_combination:
        break
    for b in range(interval_start, interval_end + 1):
        combination_num += 1
        if (a + b) == magic_number:
            x1 = a
            x2 = b
            is_combination = True
            break

if is_combination:
    print(f"Combination N:{combination_num} ({x1} + {x2} = {magic_number})")
else:
    print(f"{combination_num} combinations - neither equals {magic_number}")
