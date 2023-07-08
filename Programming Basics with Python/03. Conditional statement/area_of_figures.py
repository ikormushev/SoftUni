from math import pi

figure = input()
figure_area = 0

if figure == "square":
    square_side = float(input())
    figure_area = square_side * square_side
elif figure == "rectangle":
    rectangle_side_x = float(input())
    rectangle_side_y = float(input())
    figure_area = rectangle_side_x * rectangle_side_y
elif figure == "circle":
    circle_radius = float(input())
    figure_area = pi * (circle_radius ** 2)
elif figure == "triangle":
    triangle_side = float(input())
    triangle_height = float(input())
    figure_area = (triangle_side * triangle_height) / 2

print(f"{figure_area:.3f}")
