from math import sqrt, floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def closest_to_center(a, b, c, d):
    first_distance = sqrt(a ** 2 + b ** 2)
    second_distance = sqrt(c ** 2 + d ** 2)

    if first_distance > second_distance:
        return f"({floor(c)}, {floor(d)})"
    else:
        return f"({floor(a)}, {floor(b)})"


print(closest_to_center(a=x1, b=y1, c=x2, d=y2))
