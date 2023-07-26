free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

free_space_area = free_space_width * free_space_length * free_space_height
boxes = 0
free_space_left = free_space_area

for i in range(free_space_area):
    boxes = input()
    if boxes == "Done":
        break
    boxes_num = int(boxes)  # box_area = 1 * 1 * 1
    free_space_left -= boxes_num
    if free_space_left < 0:
        free_space_left = abs(free_space_left)
        print(f"No more free space! You need {free_space_left} Cubic meters more")
        break

if boxes == "Done" and free_space_left >= 0:
    print(f"{free_space_left} Cubic meters left.")
