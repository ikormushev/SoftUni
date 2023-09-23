number = int(input())

for n in range(1, number + 1):
    digits_sum = 0
    is_special_number = False
    for i in range(len(str(n))):
        digits_sum += int(str(n)[i])

    if digits_sum in [5, 7, 11]:
        is_special_number = True

    print(f"{n} -> {is_special_number}")
