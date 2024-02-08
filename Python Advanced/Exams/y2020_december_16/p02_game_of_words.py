possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

initial_string = list(input())
field_size = int(input())

field = []
player_position = []

for row in range(field_size):
    given_row = input()
    field.append([])
    for col in range(field_size):
        if given_row[col] == "P":
            player_position = [row, col]
        field[row].append(given_row[col])

commands_num = int(input())

for _ in range(commands_num):
    move = input()
    move_row, move_col = possible_moves[move]
    current_row, current_col = player_position

    new_row = move_row + current_row
    new_col = move_col + current_col
    if (0 <= new_row < field_size) and (0 <= new_col < field_size):
        current_element = field[new_row][new_col]
        if current_element.isalpha():
            initial_string.append(current_element)
        field[current_row][current_col] = "-"
        field[new_row][new_col] = "P"
        player_position = [new_row, new_col]
    else:
        if initial_string:
            initial_string.pop()

print("".join(initial_string))
[print(''.join(row)) for row in field]
