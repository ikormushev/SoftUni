space_width = int(input())
length_width = int(input())
height_width = int(input())

space_area = space_width * length_width * height_width
computers_num = 0
computers_area = 0
space_left = 0

for _ in range(space_area):
    computers_num = input()
    if computers_num == "Done":
        break
    computers_num = int(computers_num)
    computers_area += computers_num
    space_left = space_area - computers_area
    if space_left < 0:
        print(f"No more free space! You need {abs(space_left)} "
              f"Cubic meters more.")
        break

if computers_num == "Done" and space_left >= 0:
    print(f"{space_left} Cubic meters left.")

