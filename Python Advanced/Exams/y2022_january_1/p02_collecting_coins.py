field_size = int(input())
possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

field = []
player_position = []
player_path = []

for row in range(field_size):
    given_row = input().split()
    field.append([])
    for col in range(field_size):
        if given_row[col] == "P":
            player_position = [row, col]
            player_path.append(player_position)

        if given_row[col].isnumeric():
            field[row].append(int(given_row[col]))
        else:
            field[row].append(given_row[col])

total_coins = 0

while total_coins < 100:
    command = input()

    move_row, move_col = possible_moves[command]
    player_row, player_col = player_position
    new_row = move_row + player_row
    new_col = move_col + player_col
    if not (0 <= new_row < field_size) or not (0 <= new_col < field_size):
        if new_row < 0:
            new_row = field_size - 1
        elif new_row >= field_size:
            new_row = 0

        if new_col < 0:
            new_col = field_size - 1
        elif new_col >= field_size:
            new_col = 0

    field[player_row][player_col] = 0
    current_element = field[new_row][new_col]
    player_path.append([new_row, new_col])

    if current_element == "X":
        total_coins //= 2
        print(f"Game over! You've collected {total_coins} coins.")
        break
    else:
        field[new_row][new_col] = 0
        total_coins += current_element

    field[new_row][new_col] = "P"
    player_position = [new_row, new_col]

if total_coins >= 100:
    print(f"You won! You've collected {total_coins} coins.")

print("Your path:")
[print(x) for x in player_path]
