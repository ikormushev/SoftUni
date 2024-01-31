matrix_size = int(input())
racing_number = input()

matrix = [input().split() for x in range(matrix_size)]
first_tunnel, second_tunnel = [[row, col] for row in range(matrix_size)
                               for col in range(matrix_size) if matrix[row][col] == "T"]
possible_directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

car_coordinates = [0, 0]
kilometers_passed = 0
finish_line_reached = False

while not finish_line_reached:
    direction = input()
    if direction == "End":
        print(f"Racing car {racing_number} DNF.")
        break

    move_row, move_col = possible_directions[direction]
    car_row, car_col = car_coordinates
    new_row = move_row + car_row
    new_col = move_col + car_col

    if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:
        kilometers_passed += 10

        if matrix[new_row][new_col] == "T":
            kilometers_passed += 20
            matrix[new_row][new_col] = "."
            if [new_row, new_col] == first_tunnel:
                new_row, new_col = second_tunnel
            elif [new_row, new_col] == second_tunnel:
                new_row, new_col = first_tunnel

        elif matrix[new_row][new_col] == "F":
            print(f"Racing car {racing_number} finished the stage!")
            finish_line_reached = True

        matrix[new_row][new_col] = "."
        car_coordinates = [new_row, new_col]

car_row, car_col = car_coordinates
matrix[car_row][car_col] = "C"

print(f"Distance covered {kilometers_passed} km.")
[print("".join(x)) for x in matrix]
