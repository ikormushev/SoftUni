interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_num = 0
is_number_found = False

for n1 in range(interval_start, interval_end + 1):
    if is_number_found:
        break
    for n2 in range(interval_start, interval_end + 1):
        combination_num += 1
        if (n1 + n2) == magic_number:
            print(f"Combination N:{combination_num} ({n1} + {n2} = {magic_number})")
            is_number_found = True
            break

if not is_number_found:
    print(f"{combination_num} combinations - neither equals {magic_number}")
