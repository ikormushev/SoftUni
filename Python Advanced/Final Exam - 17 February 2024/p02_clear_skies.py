possible_directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

matrix_size = int(input())

matrix = []
current_position = []
enemy_planes_count = 0

for row in range(matrix_size):
    given_row = input()
    matrix.append([])
    for col in range(matrix_size):
        if given_row[col] == "J":
            current_position = [row, col]
        elif given_row[col] == "E":
            enemy_planes_count += 1
        matrix[row].append(given_row[col])

initial_armor = 300
armor_left = initial_armor
enemy_planes_left = enemy_planes_count
mission_accomplished = False

while enemy_planes_left > 0 and armor_left > 0:
    direction = input()
    direction_row, direction_col = possible_directions[direction]
    current_row, current_col = current_position

    new_row = direction_row + current_row
    new_col = direction_col + current_col

    if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:
        current_element = matrix[new_row][new_col]

        if current_element == "E":
            matrix[new_row][new_col] = "-"
            enemy_planes_left -= 1
            if enemy_planes_left == 0:
                mission_accomplished = True
            else:
                armor_left -= 100

        elif current_element == "R":
            armor_left = 300

        matrix[current_row][current_col] = "-"
        matrix[new_row][new_col] = "J"
        current_position = [new_row, new_col]

if mission_accomplished:
    print("Mission accomplished, you neutralized the aerial threat!")
else:
    print(f"Mission failed, your jetfighter was shot down! "
          f"Last coordinates [{current_position[0]}, {current_position[1]}]!")

[print("".join(row)) for row in matrix]
