matrix_size = 5
possible_movements = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

matrix = []
our_position = []
total_targets = 0

for row in range(matrix_size):
    given_row = input().split()
    matrix.append([])
    for col in range(matrix_size):
        if given_row[col] == "A":
            our_position = [row, col]
        elif given_row[col] == "x":
            total_targets += 1
        matrix[row].append(given_row[col])

commands_num = int(input())
commands_passed = 0
targets_hit = []

while commands_passed < commands_num and total_targets:
    command = input().split()
    commands_passed += 1
    command_name = command[0]
    move = command[1]

    current_row, current_col = our_position
    if command_name == "move":
        steps = int(command[2])
        move_row, move_col = possible_movements[move]
        new_row = current_row + move_row * steps
        new_col = current_col + move_col * steps
        if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:
            if matrix[new_row][new_col] == ".":
                our_position = [new_row, new_col]

    elif command_name == "shoot":
        target_found = False
        shoot_row = current_row
        shoot_col = current_col

        while not target_found:
            move_row, move_col = possible_movements[move]
            new_row = shoot_row + move_row
            new_col = shoot_col + move_col
            if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:
                if matrix[new_row][new_col] == "x":
                    total_targets -= 1
                    matrix[new_row][new_col] = "."
                    targets_hit.append([new_row, new_col])
                    target_found = True
                else:
                    shoot_row = new_row
                    shoot_col = new_col
            else:
                break

if not total_targets:
    print(f"Training completed! All {len(targets_hit)} targets hit.")
else:
    print(f"Training not completed! {total_targets} targets left.")

[print(x) for x in targets_hit]
