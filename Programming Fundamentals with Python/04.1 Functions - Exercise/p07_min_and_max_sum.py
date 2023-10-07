numbers = list(map(int, input().split(" ")))


def minimum_number(x):
    return min(x)


def maximum_number(y):
    return max(y)


def sum_of_numbers(z):
    return sum(z)


print(f"The minimum number is {minimum_number(numbers)}")
print(f"The maximum number is {maximum_number(numbers)}")
print(f"The sum number is: {sum_of_numbers(numbers)}")
