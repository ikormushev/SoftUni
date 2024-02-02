matrix_size = 6
possible_directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

matrix = [[x for x in input().split()] for _ in range(matrix_size)]

positions = input().split(", ")
first_row = int(positions[0][1:])
first_col = int(positions[1][:-1])
current_position = [first_row, first_col]

while True:
    command = input()
    if command == "Stop":
        break
    new_command = command.split(", ")
    direction = new_command[1]

    current_row, current_col = current_position
    move_row, move_col = possible_directions[direction]
    new_row = current_row + move_row
    new_col = current_col + move_col

    if not (0 <= new_row < matrix_size) or not (0 <= new_col < matrix_size):
        continue
    current_position = [new_row, new_col]

    if new_command[0] == "Create":
        given_value = new_command[2]
        if matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = given_value

    elif new_command[0] == "Update":
        given_value = new_command[2]
        if matrix[new_row][new_col] != ".":
            matrix[new_row][new_col] = given_value

    elif new_command[0] == "Delete":
        if matrix[new_row][new_col] != ".":
            matrix[new_row][new_col] = "."

    elif new_command[0] == "Read":
        if matrix[new_row][new_col] != ".":
            print(matrix[new_row][new_col])

[print(" ".join(row)) for row in matrix]
