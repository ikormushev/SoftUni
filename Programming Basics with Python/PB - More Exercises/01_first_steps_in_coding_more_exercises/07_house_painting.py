x = float(input())
y = float(input())
h = float(input())

green_paint_lt_to_m = 3.4 # кв.м
red_paint_lt_to_m = 4.3 # кв.м

door_area = 1.2 * 2
front_wall_area = x * x
back_wall_area = x * x
front_and_back_wall_area_for_painting = front_wall_area + back_wall_area - door_area

window_area = 1.5 * 1.5
side_walls_area = 2 * (x * y)
side_wall_area_for_painting = side_walls_area - 2 * window_area

roof_rectangles_area = 2 * (x * y)
roof_triangles_area = 2 * (x * h / 2)
roof_area_for_painting = roof_rectangles_area + roof_triangles_area

green_paint = (front_and_back_wall_area_for_painting + side_wall_area_for_painting) / green_paint_lt_to_m
red_paint = roof_area_for_painting / red_paint_lt_to_m

print('{:0.2f}'.format(green_paint))
print('{:0.2f}'.format(red_paint))
