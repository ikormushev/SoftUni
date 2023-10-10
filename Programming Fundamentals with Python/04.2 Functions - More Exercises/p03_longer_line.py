from math import sqrt, floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def line_length(a, b, c, d):
    length = sqrt((c - a) ** 2 + (d - b) ** 2)
    return length


def closest_to_center(e, f, g, h):
    first_distance = sqrt(e ** 2 + f ** 2)
    second_distance = sqrt(g ** 2 + h ** 2)

    if first_distance > second_distance:
        return f"({floor(g)}, {floor(h)})({floor(e)}, {floor(f)})"
    else:
        return f"({floor(e)}, {floor(f)})({floor(g)}, {floor(h)})"


def longer_line_from_two():
    if line_length(x1, y1, x2, y2) >= line_length(x3, y3, x4, y4):
        return closest_to_center(e=x1, f=y1, g=x2, h=y2)
    else:
        return closest_to_center(e=x3, f=y3, g=x4, h=y4)


print(longer_line_from_two())
