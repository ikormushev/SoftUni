from collections import deque

matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for row in range(matrix_size)]
bomb_coordinates = deque([[int(y) for y in x.split(",")] for x in input().split()])

possible_explosions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

while bomb_coordinates:
    bomb_row, bomb_col = bomb_coordinates.popleft()
    bomb_value = matrix[bomb_row][bomb_col]
    if bomb_value <= 0:
        continue

    for row, column in possible_explosions:
        current_row = bomb_row + row
        current_column = bomb_col + column
        if 0 <= current_row < matrix_size and 0 <= current_column < matrix_size:
            if matrix[current_row][current_column] > 0:
                matrix[current_row][current_column] -= bomb_value

alive_cells_num = 0
alive_cells_sum = 0

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] > 0:
            alive_cells_num += 1
            alive_cells_sum += matrix[row][col]

print(f"Alive cells: {alive_cells_num}")
print(f"Sum: {alive_cells_sum}")
[print(*row) for row in matrix]
