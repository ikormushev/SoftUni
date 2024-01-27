field_size = int(input())

field = []
movement = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

bunny_position = []

for row in range(field_size):
    given_row = input().split()
    field.append([])
    for col in range(field_size):
        field[row].append(given_row[col])
        if given_row[col] == "B":
            bunny_position = [row, col]

max_eggs_move = ""
max_eggs_path = []
max_eggs_count = float("-inf")

for (move, indexes) in movement.items():
    current_row, current_col = bunny_position
    current_eggs_count = 0
    current_path = []

    move_row_index, move_col_index = indexes
    while True:
        current_row += move_row_index
        current_col += move_col_index
        if 0 <= current_row < field_size and 0 <= current_col < field_size:
            if field[current_row][current_col] == "X":
                break
            current_eggs_count += int(field[current_row][current_col])
            current_path.append([current_row, current_col])
        else:
            break
    if current_eggs_count > max_eggs_count and current_path:
        max_eggs_count = current_eggs_count
        max_eggs_move = move
        max_eggs_path = current_path

print(max_eggs_move)
[print(x) for x in max_eggs_path]
print(max_eggs_count)
