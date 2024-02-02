from collections import deque

possible_position = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "top-left": [-1, -1],
    "top-right": [-1, 1],
    "down-left": [1, -1],
    "down-right": [1, 1],
}

mines_field_size = int(input())
bombs_to_place = int(input())

bombs = deque()
matrix = [[0 for _ in range(mines_field_size)] for _ in range(mines_field_size)]

for _ in range(bombs_to_place):
    coordinates = input().split(", ")
    row = int(coordinates[0][1:])
    col = int(coordinates[1][:-1])
    bombs.append([row, col])

while bombs:
    bomb_row, bomb_col = bombs.popleft()
    matrix[bomb_row][bomb_col] = "*"
    for (pos, coordinates) in possible_position.items():
        move_row, move_col = coordinates
        new_row = move_row + bomb_row
        new_col = move_col + bomb_col
        if 0 <= new_row < mines_field_size and 0 <= new_col < mines_field_size:
            current_element = matrix[new_row][new_col]
            if isinstance(current_element, int):
                matrix[new_row][new_col] += 1

for row in range(mines_field_size):
    for col in range(mines_field_size):
        if col == mines_field_size - 1:
            print(matrix[row][col])
        else:
            print(matrix[row][col], end=" ")
