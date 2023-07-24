from math import floor

hall_length_m = float(input())
hall_width_m = float(input())
wardrobe_side_m = float(input())

hall_area = hall_length_m * hall_width_m
bench_area = hall_area / 10
wardrobe_area = wardrobe_side_m * wardrobe_side_m

dancer_square_cm = 40
dancer_square_m = dancer_square_cm / 10000  # 1 square m = 10 000 square cm
dancing_space_square_cm = 7000
dancing_space_square_m = dancing_space_square_cm / 10000  # 1 square m = 10 000 square cm

dancer_space_square_m = dancer_square_m + dancing_space_square_m

hall_free_space = hall_area - bench_area - wardrobe_area
dancers = hall_free_space / dancer_space_square_m

print(floor(dancers))
