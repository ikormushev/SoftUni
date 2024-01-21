matrix_dimensions = input().split()
matrix_rows = int(matrix_dimensions[0])
matrix_columns = int(matrix_dimensions[1])

matrix = [input().split() for row in range(matrix_rows)]

square_matrix_num = 0

for row in range(matrix_rows - 1):
    for col in range(matrix_columns - 1):
        first_el = matrix[row][col]
        second_el = matrix[row][col + 1]
        third_el = matrix[row + 1][col]
        fourth_el = matrix[row + 1][col + 1]
        if first_el == second_el == third_el == fourth_el:
            square_matrix_num += 1

print(square_matrix_num)