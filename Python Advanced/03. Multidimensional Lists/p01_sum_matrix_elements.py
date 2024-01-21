matrix_info = input().split(", ")
matrix_rows = int(matrix_info[0])
matrix_columns = int(matrix_info[1])

matrix = []
numbers_sum = 0

for _ in range(matrix_rows):
    columns = [int(x) for x in input().split(", ")]
    numbers_sum += sum(columns)
    matrix.append(columns)

print(numbers_sum)
print(matrix)
