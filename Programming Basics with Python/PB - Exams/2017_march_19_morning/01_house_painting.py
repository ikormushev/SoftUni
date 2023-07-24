x = float(input())  # house_height
y = float(input())  # side_wall_length
h = float(input())  # roof_triangle_wall_height

green_paint_square_m_per_lt = 3.4
red_paint_square_m_per_lt = 4.3

front_wall_area = x * x
back_wall_area = x * x

door_width_m = 1.2
door_height_m = 2
door_area = door_width_m * door_height_m

front_wall_area_without_door = front_wall_area - door_area
front_and_back_wall_area = front_wall_area_without_door + back_wall_area

side_walls_area = 2 * (x * y)
window_side_m = 1.5
windows_area = 2 * (window_side_m * window_side_m)
side_walls_area_without_windows = side_walls_area - windows_area

roof_rectangles_area = 2 * (x * y)
roof_triangles_area = 2 * (x * h / 2)
roof_area = roof_rectangles_area + roof_triangles_area

walls_painting = (front_and_back_wall_area + side_walls_area_without_windows) / green_paint_square_m_per_lt
roof_painting = roof_area / red_paint_square_m_per_lt

print('{0:.2f}'.format(walls_painting))
print('{0:.2f}'.format(roof_painting))
