from math import ceil

wall_height = int(input())
wall_width = int(input())
wall_area_not_for_paining_percentage = int(input()) / 100

walls_area = wall_height * wall_width * 4
walls_area_left = ceil(walls_area * (1 - wall_area_not_for_paining_percentage))

while True:
    command = input()
    if command == "Tired!":
        print(f"{walls_area_left} quadratic m left.")
        break
    paint_lt = int(command)
    walls_area_left -= paint_lt
    if walls_area_left <= 0:
        if walls_area_left == 0:
            print(f"All walls are painted! Great job, Pesho!")
        else:
            print(f"All walls are painted and you have {abs(walls_area_left)} l paint left!")
        break
