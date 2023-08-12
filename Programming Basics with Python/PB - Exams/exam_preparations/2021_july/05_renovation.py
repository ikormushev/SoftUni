from math import ceil

wall_height = int(input())
wall_width = int(input())
no_paint_percentage = int(input()) / 100

walls_area = wall_height * wall_width * 4
no_paint_area = ceil(no_paint_percentage * walls_area)
walls_area_left = walls_area - no_paint_area

while True:
    command = input()
    if command == "Tired!":
        print(f"{walls_area_left} quadratic m left.")
        break
    paint_lt = int(command)
    walls_area_left -= paint_lt
    if walls_area_left <= 0:
        if walls_area_left == 0:
            print("All walls are painted! Great job, Pesho!")
            break
        else:
            print(f"All walls are painted and you have {abs(walls_area_left)} l paint left!")
            break
