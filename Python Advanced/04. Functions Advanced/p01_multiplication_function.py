def multiply(*args):
    multiplication = 1
    for number in args:
        multiplication *= int(number)
    return multiplication

# print(multiply(1, 4, 5))  # 20
# print(multiply(4, 5, 6, 1, 3))  # 360
# print(multiply(2, 0, 1000, 5000))  # 0
