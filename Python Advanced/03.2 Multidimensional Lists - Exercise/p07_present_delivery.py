presents_num = int(input())
neighborhood_size = int(input())
possible_movements = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

neighborhood = []
santa_coordinates = []
total_nice_kids = 0

for row in range(neighborhood_size):
    given_row = input().split()
    neighborhood.append([])
    for col in range(neighborhood_size):
        if given_row[col] == "S":
            santa_coordinates = [row, col]
        elif given_row[col] == "V":
            total_nice_kids += 1
        neighborhood[row].append(given_row[col])

nice_kids_pleased = 0

while presents_num:
    command = input()
    if command == "Christmas morning":
        break
    move_row, move_col = possible_movements[command]
    current_row, current_col = santa_coordinates
    new_row = current_row + move_row
    new_col = current_col + move_col
    if 0 <= new_row < neighborhood_size and 0 <= new_col < neighborhood_size:
        neighborhood[current_row][current_col] = "-"
        santa_coordinates = [new_row, new_col]
        if neighborhood[new_row][new_col] == "C":
            for (move, coordinates) in possible_movements.items():
                move_row, move_col = coordinates
                current_row, current_col = santa_coordinates
                new_row = current_row + move_row
                new_col = current_col + move_col
                if 0 <= new_row < neighborhood_size and 0 <= new_col < neighborhood_size:
                    matrix_element = neighborhood[new_row][new_col]
                    if matrix_element in ["V", "X"]:
                        if matrix_element == "V":
                            nice_kids_pleased += 1
                        presents_num -= 1
                        neighborhood[new_row][new_col] = "-"
                        if presents_num == 0:
                            break
        elif neighborhood[new_row][new_col] == "V":
            presents_num -= 1
            nice_kids_pleased += 1
        neighborhood[new_row][new_col] = "-"

neighborhood[santa_coordinates[0]][santa_coordinates[1]] = "S"

nice_kids_difference = total_nice_kids - nice_kids_pleased
if nice_kids_difference and not presents_num:
    print("Santa ran out of presents!")

[print(" ".join(x)) for x in neighborhood]
if not total_nice_kids - nice_kids_pleased:
    print(f"Good job, Santa! {nice_kids_pleased} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_difference} nice kid/s.")
