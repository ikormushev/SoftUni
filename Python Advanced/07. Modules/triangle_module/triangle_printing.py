def print_triangle(number):
    print_triangle_top(number)
    print_triangle_bottom(number)


def print_triangle_top(number):
    for i in range(1, number + 2):
        for y in range(1, i):
            if y == i - 1:
                print(y)
            else:
                print(y, end=" ")


def print_triangle_bottom(number):
    for i in range(number, 0, -1):
        for y in range(1, i):
            if y == i - 1:
                print(y)
            else:
                print(y, end=" ")
