matrix_size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]

given_commands = {
    "Add": lambda x, y:  x + y,
    "Subtract": lambda x, y:  x - y
}
command = input()

while command != "END":
    new_command = command.split()
    operation = new_command[0]
    row, col, value = [int(x) for x in new_command[1:]]
    if not (0 <= row < matrix_size) or not (0 <= col < matrix_size):
        print("Invalid coordinates")
        command = input()
        continue
    matrix[row][col] = given_commands[operation](matrix[row][col], value)
    command = input()

[print(*row) for row in matrix]