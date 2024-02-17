from collections import deque

rows_num = int(input())

field = [[int(x) for x in input().split()] for _ in range(rows_num)]
attacked_squares = deque(input().split())

ships_destroyed = 0

while attacked_squares:
    current_row, current_col = [int(x) for x in attacked_squares.popleft().split("-")]
    current_ship = field[current_row][current_col]
    if current_ship <= 0:
        continue

    current_ship -= 1
    field[current_row][current_col] = current_ship

    if current_ship == 0:
        ships_destroyed += 1

print(ships_destroyed)
