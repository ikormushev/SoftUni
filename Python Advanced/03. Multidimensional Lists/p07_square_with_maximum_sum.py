matrix_size = input().split(", ")
matrix_rows = int(matrix_size[0])
matrix_columns = int(matrix_size[1])

matrix = [[int(x) for x in input().split(", ")] for _ in range(matrix_rows)]

top_left_submatrix = [[matrix[0][0], matrix[0][1]], [matrix[1][0], matrix[1][1]]]
max_sum = matrix[0][0] + matrix[0][1] + matrix[1][0] + matrix[1][1]

for row in range(matrix_rows - 1):
    for col in range(matrix_columns - 1):
        current_sum = matrix[row][col] + matrix[row + 1][col] + matrix[row][col + 1] + matrix[row + 1][col + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            top_left_submatrix = [[matrix[row][col], matrix[row][col + 1]],
                                  [matrix[row + 1][col], matrix[row + 1][col + 1]]]

print(*top_left_submatrix[0])
print(*top_left_submatrix[1])
print(max_sum)
