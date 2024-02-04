possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

matrix_size = int(input())

matrix = []
snake_position = []
burrows_positions = []

for row in range(matrix_size):
    given_row = input()
    matrix.append([])
    for col in range(matrix_size):
        if given_row[col] == "S":
            snake_position = [row, col]
        elif given_row[col] == "B":
            burrows_positions.append([row, col])
        matrix[row].append(given_row[col])

food_quantity = 0

while food_quantity < 10:
    move = input()
    move_row, move_col = possible_moves[move]
    snake_row, snake_col = snake_position

    new_row = move_row + snake_row
    new_col = move_col + snake_col

    matrix[snake_row][snake_col] = "."

    if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:
        if matrix[new_row][new_col] == "B":
            first_burrow = [new_row, new_col]
            second_burrow = burrows_positions[1] if burrows_positions[1] != first_burrow else burrows_positions[0]
            matrix[new_row][new_col] = "."
            new_row, new_col = second_burrow
        elif matrix[new_row][new_col] == "*":
            food_quantity += 1
        matrix[new_row][new_col] = "S"
        snake_position = [new_row, new_col]

    else:
        print("Game over!")
        break

if food_quantity >= 10:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_quantity}")
[print("".join(row)) for row in matrix]

