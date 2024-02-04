possible_moves = {
    "up": lambda x: [-x, 0],
    "down": lambda x: [x, 0],
    "left": lambda x: [0, -x],
    "right": lambda x: [0, x]
}

field_size = int(input())

field = []
current_position = []
total_targets_count = 0

for row in range(field_size):
    given_row = input().split()
    field.append([])
    for col in range(field_size):
        if given_row[col] == "p":
            current_position = [row, col]
        elif given_row[col] == "t":
            total_targets_count += 1
        field[row].append(given_row[col])

targets_killed = 0
commands_count = int(input())

all_targets_shot = False
for _ in range(commands_count):
    command = input().split()
    steps = int(command[2])
    current_row, current_col = current_position

    if command[0] == "move":
        move_row, move_col = possible_moves[command[1]](steps)
        new_row = move_row + current_row
        new_col = move_col + current_col
        if 0 <= new_row < field_size and 0 <= new_col < field_size:
            if field[new_row][new_col] == ".":
                field[current_row][current_col] = "."
                current_position = [new_row, new_col]
                field[new_row][new_col] = "p"

    elif command[0] == "shoot":
        shoot_row, shoot_col = possible_moves[command[1]](steps)
        new_row = shoot_row + current_row
        new_col = shoot_col + current_col
        if 0 <= new_row < field_size and 0 <= new_col < field_size:
            if field[new_row][new_col] == "t":
                targets_killed += 1
            field[new_row][new_col] = "x"
            if targets_killed == total_targets_count:
                all_targets_shot = True
                break

if all_targets_shot:
    print(f"Mission accomplished! All {total_targets_count} targets destroyed.")
else:
    print(f"Mission failed! {total_targets_count - targets_killed} targets left.")

[print(" ".join(row)) for row in field]
