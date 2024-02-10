def move_check(position, area_size):
    if position < 0:
        position = area_size - 1
    elif position >= area_size:
        position = 0

    return position


possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

fishing_area_size = int(input())

fishing_area = []
current_pos = []

tons_fish_needed = 20
tons_fish_collected = 0

for row in range(fishing_area_size):
    given_row = input()
    fishing_area.append([])
    for col in range(fishing_area_size):
        if given_row[col] == "S":
            current_pos = [row, col]
        fishing_area[row].append(given_row[col])

fallen_into_whirlpool = False

while True:
    command = input()
    if command == "collect the nets":
        break
    move_row, move_col = possible_moves[command]
    current_row, current_col = current_pos

    new_row = move_row + current_row
    new_col = move_col + current_col

    new_row = move_check(new_row, fishing_area_size)
    new_col = move_check(new_col, fishing_area_size)

    fishing_area[current_row][current_col] = "-"

    current_pos = [new_row, new_col]
    current_element = fishing_area[new_row][new_col]

    if current_element == "W":
        fallen_into_whirlpool = True
        break
    elif current_element.isnumeric():
        tons_fish_collected += int(current_element)
    fishing_area[new_row][new_col] = "S"

if fallen_into_whirlpool:
    last_row, last_col = current_pos
    print(f"You fell into a whirlpool! "
          f"The ship sank and you lost the fish you caught. "
          f"Last coordinates of the ship: [{last_row},{last_col}]")
else:
    if tons_fish_collected >= tons_fish_needed:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! "
              f"You need {tons_fish_needed - tons_fish_collected} tons of fish more.")

    if tons_fish_collected:
        print(f"Amount of fish caught: {tons_fish_collected} tons.")

    [print("".join(row)) for row in fishing_area]
