possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

matrix_rows, matrix_cols = [int(x) for x in input().split(", ")]

matrix = []
current_position = []
christmas_items = {
    "Christmas decorations": {"limit": 0, "count": 0},
    "Gifts": {"limit": 0, "count": 0},
    "Cookies": {"limit": 0, "count": 0},
}

for row in range(matrix_rows):
    given_row = input().split()
    matrix.append([])
    for col in range(matrix_cols):
        current_element = given_row[col]

        if current_element == "Y":
            current_position = [row, col]
        elif current_element == "D":
            christmas_items["Christmas decorations"]["limit"] += 1
        elif current_element == "G":
            christmas_items["Gifts"]["limit"] += 1
        elif current_element == "C":
            christmas_items["Cookies"]["limit"] += 1

        matrix[row].append(given_row[col])

are_all_items_collected = False

while not are_all_items_collected:
    command = input()
    if command == "End":
        break
    move_command, move_steps = command.split("-")
    move_row, move_col = possible_moves[move_command]

    for _ in range(int(move_steps)):
        current_row, current_col = current_position
        new_row = current_row + move_row
        new_col = current_col + move_col

        if not (0 <= new_row < matrix_rows) or not (0 <= new_col < matrix_cols):
            if new_row < 0:
                new_row = matrix_rows - 1
            elif new_row >= matrix_rows:
                new_row = 0

            if new_col < 0:
                new_col = matrix_cols - 1
            elif new_col >= matrix_cols:
                new_col = 0

        current_element = matrix[new_row][new_col]
        if current_element == "D":
            christmas_items["Christmas decorations"]["count"] += 1
        elif current_element == "G":
            christmas_items["Gifts"]["count"] += 1
        elif current_element == "C":
            christmas_items["Cookies"]["count"] += 1

        matrix[current_row][current_col] = "x"
        matrix[new_row][new_col] = "Y"
        current_position = [new_row, new_col]

        all_items_collected = []
        for (item, info) in christmas_items.items():
            all_items_collected.append(info["limit"] == info["count"])

        if all(all_items_collected):
            are_all_items_collected = True
            print("Merry Christmas!")
            break

print("You've collected:")
[print(f"- {info['count']} {item}") for (item, info) in christmas_items.items()]
[print(" ".join(row)) for row in matrix]
