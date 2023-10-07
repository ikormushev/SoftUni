number = int(input())
divider = int(input())


def factorials_of_number(n):
    number_factors = []

    if n > 0:
        for i in range(1, n + 1):
            number_factors.append(i)
    elif n == 0:
        number_factors.append(1)

    return number_factors


def factorial(factors):
    total_factorial = 1  # if it is equal to 0, we cannot multiply it
    factorials = factors
    for y in range(len(factorials)):
        total_factorial *= factorials[y]

    return total_factorial


def task_division():
    return factorial(factorials_of_number(number)) / factorial(factorials_of_number(divider))


print(f"{task_division():.2f}")
