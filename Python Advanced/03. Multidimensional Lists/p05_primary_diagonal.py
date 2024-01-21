matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]
primary_diagonal_sum = 0

for row_num in range(matrix_size):
    for column_num in range(matrix_size):
        if row_num == column_num:
            primary_diagonal_sum += matrix[row_num][column_num]

print(primary_diagonal_sum)
