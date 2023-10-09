first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(a, b):
    result = a + b
    return result


def subtract(c, d):
    subtraction = c - d
    return subtraction


def add_and_subtract(a, b, c):
    result = subtract(sum_numbers(a, b), c)
    return result


print(add_and_subtract(first_number, second_number, third_number))
