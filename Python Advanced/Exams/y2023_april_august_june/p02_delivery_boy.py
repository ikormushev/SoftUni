possible_movements = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

field_rows, field_cols = [int(x) for x in input().split()]

field = []
starting_position = []
delivery_boy_position = []

for row in range(field_rows):
    given_row = input()
    field.append([])
    for col in range(field_cols):
        if given_row[col] == "B":
            starting_position = [row, col]
        field[row].append(given_row[col])

delivery_boy_position = starting_position
restaurant_reached = False

while True:
    move = input()
    move_row, move_col = possible_movements[move]
    current_row, current_col = delivery_boy_position
    new_row = move_row + current_row
    new_col = move_col + current_col

    if 0 <= new_row < field_rows and 0 <= new_col < field_cols:
        if field[new_row][new_col] == "P" and not restaurant_reached:
            restaurant_reached = True
            field[new_row][new_col] = "R"
            print("Pizza is collected. 10 minutes for delivery.")

        elif field[new_row][new_col] == "*":
            continue

        elif field[new_row][new_col] == "A":
            field[new_row][new_col] = "P"
            print("Pizza is delivered on time! Next order...")
            break

        elif field[new_row][new_col] == "-":
            field[new_row][new_col] = "."

        delivery_boy_position = [new_row, new_col]

    else:
        start_row, start_col = starting_position
        field[start_row][start_col] = " "
        print("The delivery is late. Order is canceled.")
        break

[print(''.join(row)) for row in field]
