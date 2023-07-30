free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

free_space_area = free_space_width * free_space_length * free_space_height
command = 0
free_space = free_space_area

while free_space > 0:
    command = input()
    if command == "Done":
        break
    boxes = int(command)
    free_space -= boxes

if command == "Done" and free_space > 0:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
