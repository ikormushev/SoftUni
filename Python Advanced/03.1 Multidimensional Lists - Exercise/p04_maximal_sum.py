matrix_size = input().split()
matrix_rows = int(matrix_size[0])
matrix_columns = int(matrix_size[1])

matrix = [[int(x) for x in input().split()] for row in range(matrix_rows)]

submatrix = []
max_sum = 0

for row in range(matrix_rows - 2):
    for col in range(matrix_columns - 2):
        first_row = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]]
        second_row = [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]]
        third_row = [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if (current_sum > max_sum) or (row == 0 and col == 0):
            submatrix = [first_row, second_row, third_row]
            max_sum = current_sum

print(f"Sum = {max_sum}")
[print(*x) for x in submatrix]
