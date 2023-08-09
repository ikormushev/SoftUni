place_width = int(input())
place_length = int(input())
place_height = int(input())

place_area = place_width * place_length * place_height
place_left = place_area
flag = False

while True:
    command = input()
    if command == "Done":
        flag = True
        break
    cartons = int(command)
    place_left -= cartons
    if place_left <= 0:
        break

if flag and place_left > 0:
    print(f"{place_left} Cubic meters left.")
else:
    print(f"No more free space! You need "
          f"{abs(place_left)} Cubic meters more.")
