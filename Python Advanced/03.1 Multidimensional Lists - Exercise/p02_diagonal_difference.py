matrix_size = int(input())

matrix = [[int(x) for x in input().split()] for row in range(matrix_size)]
primary_diagonal = [[matrix[row][col] for col in range(matrix_size) if col == row][0] for row in range(matrix_size)]
secondary_diagonal = [[matrix[row][col] for col in range(matrix_size - 1, -1, -1)
                       if col == matrix_size - row - 1][0] for row in range(matrix_size)]

sum_difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(sum_difference)
