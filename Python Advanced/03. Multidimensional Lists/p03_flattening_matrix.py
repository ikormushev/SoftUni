matrix_rows_num = int(input())
matrix = [[int(x) for x in input().split(", ")] for row in range(matrix_rows_num)]
flattened_matrix = [number for row in matrix for number in row]

print(flattened_matrix)
