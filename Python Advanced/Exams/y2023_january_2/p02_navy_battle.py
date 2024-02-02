battlefield_size = int(input())

possible_directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

battlefield = []
submarine_coordinates = []
total_battle_cruisers = 0

for row in range(battlefield_size):
    given_row = input()
    battlefield.append([])
    for col in range(battlefield_size):
        if given_row[col] == "S":
            submarine_coordinates = [row, col]
        elif given_row[col] == "C":
            total_battle_cruisers += 1
        battlefield[row].append(given_row[col])

mines_hit = 0

while total_battle_cruisers and mines_hit < 3:
    direction = input()
    submarine_row, submarine_col = submarine_coordinates
    move_row, move_col = possible_directions[direction]
    new_row = submarine_row + move_row
    new_col = submarine_col + move_col
    if 0 <= new_row < battlefield_size and 0 <= new_col < battlefield_size:
        battlefield[submarine_row][submarine_col] = "-"
        if battlefield[new_row][new_col] == "*":
            mines_hit += 1
            if mines_hit == 3:
                print(f"Mission failed, U-9 disappeared! Last known coordinates [{new_row}, {new_col}]!")
        elif battlefield[new_row][new_col] == "C":
            total_battle_cruisers -= 1
            battlefield[new_row][new_col] = "-"
            if not total_battle_cruisers:
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

        submarine_coordinates = [new_row, new_col]

submarine_row, submarine_col = submarine_coordinates
battlefield[submarine_row][submarine_col] = "S"
[print("".join(row)) for row in battlefield]
