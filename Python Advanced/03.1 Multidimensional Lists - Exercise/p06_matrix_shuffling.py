def valid_command(command_to_check):
    command_executed = False
    if "swap" in command_to_check:
        if len(command_to_check) == 5:
            row1 = int(command_to_check[1])
            col1 = int(command_to_check[2])
            row2 = int(command_to_check[3])
            col2 = int(command_to_check[4])
            if (0 <= row1 < matrix_rows and 0 <= col1 < matrix_columns
                    and 0 <= row2 < matrix_rows and 0 <= col2 < matrix_columns):
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                [print(" ".join(x)) for x in matrix]
                command_executed = True

    if not command_executed:
        print("Invalid input!")


matrix_size = input().split()
matrix_rows = int(matrix_size[0])
matrix_columns = int(matrix_size[1])

matrix = [[x for x in input().split()] for row in range(matrix_rows)]

command = input()

while command != "END":
    command_info = command.split()
    valid_command(command_info)
    command = input()

