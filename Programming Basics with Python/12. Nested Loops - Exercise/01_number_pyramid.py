n = int(input())

starting_num = 1
is_found_n = False

for rows in range(1, n + 1):
    for colm in range(1, rows + 1):
        if starting_num > n:
            is_found_n = True
            break
        print(f"{starting_num} ", end="")
        starting_num += 1
    if is_found_n:
        break
    print()
