def numbers_searching(*args):
    sorted_numbers = sorted(args)
    min_number = sorted_numbers[0]
    max_number = sorted_numbers[-1]

    first_set = set(sorted_numbers)
    second_set = set(range(min_number, max_number + 1))
    missing_value = second_set - first_set

    duplicates = []

    for number in sorted_numbers:
        if sorted_numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return [missing_value.pop(), duplicates]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
