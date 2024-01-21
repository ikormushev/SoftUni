matrix_size = int(input())
matrix = [[x for x in list(input())] for _ in range(matrix_size)]
secret_symbol = input()
secret_symbol_coordinates = ""
symbol_found = False

for row in range(matrix_size):
    if symbol_found:
        break
    for col in range(matrix_size):
        if matrix[row][col] == secret_symbol:
            symbol_found = True
            secret_symbol_coordinates = f"({row}, {col})"

if symbol_found:
    print(secret_symbol_coordinates)
else:
    print(f"{secret_symbol} does not occur in the matrix")
