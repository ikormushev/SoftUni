from collections import deque

field_size = int(input())
commands = deque(input().split())
field = []
given_commands = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]
}

miner_position = []
total_coals = 0
route_end_reached = False

for row in range(field_size):
    given_row = input().split()
    field.append([])
    for col in range(field_size):
        field[row].append(given_row[col])
        if given_row[col] == "s":
            miner_position = [row, col]
        elif given_row[col] == "c":
            total_coals += 1

current_position = miner_position

while commands and total_coals:
    current_command = commands.popleft()
    current_row, current_col = current_position
    command_row, command_col = given_commands[current_command]
    new_row = current_row + command_row
    new_col = current_col + command_col
    if 0 <= new_row < field_size and 0 <= new_col < field_size:
        current_position = [new_row, new_col]
        if field[new_row][new_col] == "c":
            field[new_row][new_col] = "*"
            total_coals -= 1
        elif field[new_row][new_col] == "e":
            route_end_reached = True
            print(f"Game over! ({current_position[0]}, {current_position[1]})")
            break

if not total_coals:
    print(f"You collected all coal! ({current_position[0]}, {current_position[1]})")
elif total_coals and not route_end_reached and not commands:
    print(f"{total_coals} pieces of coal left. ({current_position[0]}, {current_position[1]})")
