matrix_sizes = input().split(", ")
matrix_rows = int(matrix_sizes[0])
matrix_columns = int(matrix_sizes[1])

columns_sums = [0 for x in range(matrix_columns)]
matrix = [[int(x) for x in input().split()] for _ in range(matrix_rows)]

for i in range(matrix_rows):
    row = matrix[i]
    for y in range(matrix_columns):
        column_number = row[y]
        columns_sums[y] += column_number

[print(x) for x in columns_sums]
