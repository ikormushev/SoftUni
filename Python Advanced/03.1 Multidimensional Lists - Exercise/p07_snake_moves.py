matrix_size = input().split()
matrix_rows = int(matrix_size[0])
matrix_columns = int(matrix_size[1])
matrix = [["" for col in range(matrix_columns)] for row in range(matrix_rows)]

snake = input()
snake_index = 0

for row in range(matrix_rows):
    if row % 2 == 0:
        for col in range(matrix_columns):
            matrix[row][col] = snake[snake_index]
            snake_index += 1
            if snake_index >= len(snake):
                snake_index = 0
    else:
        for col in range(matrix_columns - 1, -1, -1):
            matrix[row][col] = snake[snake_index]
            snake_index += 1
            if snake_index >= len(snake):
                snake_index = 0

[print("".join(x)) for x in matrix]
