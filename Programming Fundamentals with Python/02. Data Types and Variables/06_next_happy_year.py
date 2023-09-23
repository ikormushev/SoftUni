year = int(input())


while True:
    year += 1
    year_digits = list(str(year))
    equal_digits_num = 0

    for y in range(len(year_digits)):
        for i in range(y + 1, len(year_digits)):
            if year_digits[y] == year_digits[i]:
                equal_digits_num += 1
                break

    if equal_digits_num >= 1:
        continue
    else:
        print(year)
        break
