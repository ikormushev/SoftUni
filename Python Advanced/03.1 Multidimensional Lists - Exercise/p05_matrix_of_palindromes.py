matrix_size = input().split()
matrix_rows = int(matrix_size[0])
matrix_columns = int(matrix_size[1])

matrix = [["".join([chr(97 + row), chr(97 + row + col), chr(97 + row)]) for col in range(matrix_columns)] for row in range(matrix_rows)]

[print(" ".join(x)) for x in matrix]
