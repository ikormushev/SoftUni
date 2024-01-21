from collections import deque

lair_size = input().split()
lair_rows = int(lair_size[0])
lair_columns = int(lair_size[1])
possible_moves = {
    "L": [0, -1],
    "R": [0, 1],
    "U": [-1, 0],
    "D": [1, 0]
}

lair = []
player_position = []

for row in range(lair_rows):
    given_row = list(input())
    lair.append([])
    for col in range(lair_columns):
        lair[row].append(given_row[col])
        if given_row[col] == "P":
            player_position = [row, col]

moves = deque(list(input()))
player_out = False
player_dead = False
bunnies_coordinates = deque()

while moves and not player_out and not player_dead:
    current_move = moves.popleft()
    current_row, current_col = player_position
    move_row, move_col = possible_moves[current_move]
    new_row = current_row + move_row
    new_col = current_col + move_col
    if 0 <= new_row < lair_rows and 0 <= new_col < lair_columns:
        lair[current_row][current_col] = "."
        player_position = [new_row, new_col]
        if lair[new_row][new_col] == "B":
            player_dead = True
        else:
            lair[new_row][new_col] = "."
    else:
        player_out = True
        lair[current_row][current_col] = "."

    for row in range(lair_rows):
        for col in range(lair_columns):
            if lair[row][col] == "B":
                bunny = [row, col]
                bunnies_coordinates.append(bunny)

    new_bunnies = deque()

    while bunnies_coordinates:
        bunny_row, bunny_col = bunnies_coordinates.popleft()
        for move, coordinates in possible_moves.items():
            possible_row, possible_col = coordinates
            new_bunny_row = bunny_row + possible_row
            new_bunny_col = bunny_col + possible_col
            if 0 <= new_bunny_row < lair_rows and 0 <= new_bunny_col < lair_columns:
                lair[new_bunny_row][new_bunny_col] = "B"
                new_bunny_coordinates = [new_bunny_row, new_bunny_col]
                new_bunnies.append(new_bunny_coordinates)
                if new_bunny_coordinates == player_position:
                    player_dead = True

    bunnies_coordinates = new_bunnies

[print("".join(x)) for x in lair]

if player_out:
    print(f"won: {player_position[0]} {player_position[1]}")
if player_dead and not player_out:
    print(f"dead: {player_position[0]} {player_position[1]}")
