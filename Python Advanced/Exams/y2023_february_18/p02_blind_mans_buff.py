possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

playground_rows, playground_columns = [int(x) for x in input().split()]

playground = []
our_position = []

total_moves = 0
opponents_touched = 0
total_opponents = 0

for row in range(playground_rows):
    given_row = input().split()
    playground.append([])
    for col in range(playground_columns):
        if given_row[col] == "B":
            our_position = [row, col]
        elif given_row[col] == "P":
            total_opponents += 1
        playground[row].append(given_row[col])


while True:
    command = input()
    if command == "Finish" or total_opponents == opponents_touched:
        print("Game over!")
        print(f"Touched opponents: {opponents_touched} Moves made: {total_moves}")
        break

    move_row, move_col = possible_moves[command]
    current_row, current_col = our_position

    new_row = move_row + current_row
    new_col = move_col + current_col

    if 0 <= new_row < playground_rows and 0 <= new_col < playground_columns:
        if playground[new_row][new_col] == "O":
            continue
        elif playground[new_row][new_col] == "P":
            opponents_touched += 1
        total_moves += 1
        playground[current_row][current_col] = "-"
        playground[new_row][new_col] = "-"
        our_position = [new_row, new_col]

    else:
        continue
