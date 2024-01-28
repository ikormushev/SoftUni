from collections import deque

field_length = int(input())
commands = deque(input().split(", "))
field = []
possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

squirrel_position = []
hazelnuts_to_collect = 3

for row in range(field_length):
    given_row = list(input())
    field.append([])
    for col in range(field_length):
        if given_row[col] == "s":
            squirrel_position = [row, col]
        field[row].append(given_row[col])

hazelnuts_collected = 0

while commands:
    command = commands.popleft()
    squirrel_row, squirrel_col = squirrel_position
    move_row, move_col = possible_moves[command]
    new_row = squirrel_row + move_row
    new_col = squirrel_col + move_col

    if 0 <= new_row < field_length and 0 <= new_col < field_length:
        if field[new_row][new_col] == "h":
            hazelnuts_collected += 1
        elif field[new_row][new_col] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            break
        field[squirrel_row][squirrel_col] = "*"
        field[new_row][new_col] = "s"
        squirrel_position = [new_row, new_col]

    else:
        print("The squirrel is out of the field.")
        break

else:
    if hazelnuts_collected < hazelnuts_to_collect:
        print("There are more hazelnuts to collect.")
    else:
        print("Good job! You have collected all hazelnuts!")

print(f"Hazelnuts collected: {hazelnuts_collected}")
