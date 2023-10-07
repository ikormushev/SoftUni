number = int(input())


def odd_numbers_sum(x):
    total_odd_sum = 0
    for i in range(len(str(x))):
        if int(str(x)[i]) % 2 == 1:
            total_odd_sum += int(str(x)[i])
    return total_odd_sum


def even_numbers_sum(y):
    total_even_sum = 0
    for j in range(len(str(y))):
        if int(str(y)[j]) % 2 == 0:
            total_even_sum += int(str(y)[j])
    return total_even_sum


print(f"Odd sum = {odd_numbers_sum(number)}, "
      f"Even sum = {even_numbers_sum(number)}")

