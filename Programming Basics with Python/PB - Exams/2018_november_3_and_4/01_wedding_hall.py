from math import ceil

hall_length = float(input())
hall_width = float(input())
bar_side_m = float(input())

hall_area = hall_length * hall_width
bar_area = bar_side_m * bar_side_m
dancing = hall_area * 0.19

hall_space_left = hall_area - bar_area - dancing
possible_guests = hall_space_left / 3.2

print(f"{ceil(possible_guests)}")
