first_number = int(input())
second_number = int(input())
third_number = int(input())


def multiplication(x, y, z):
    negatives_count = 0
    numbers_list = [x, y, z]

    if x == 0 or y == 0 or z == 0:
        return "zero"

    for i in range(len(numbers_list)):
        if numbers_list[i] < 0:
            negatives_count += 1

    if negatives_count == 1 or negatives_count == 3:
        return "negative"
    else:
        return "positive"


print(multiplication(first_number, second_number, third_number))
