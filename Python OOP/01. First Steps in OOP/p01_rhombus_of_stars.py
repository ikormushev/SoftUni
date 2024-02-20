def print_top(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print(*["*"] * i)


def print_bottom(n):
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        print(*["*"] * i)


def print_rhombus(n):
    print_top(n)
    print_bottom(n)


number = int(input())
print_rhombus(number)
