cupboard_rows, cupboard_columns = [int(x) for x in input().split(",")]

cupboard = []
mouse_coordinates = []
possible_directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}
total_cheeses = 0

for row in range(cupboard_rows):
    given_row = list(input())
    cupboard.append([])
    for column in range(cupboard_columns):
        if given_row[column] == "M":
            mouse_coordinates = [row, column]
        elif given_row[column] == "C":
            total_cheeses += 1
        cupboard[row].append(given_row[column])

cheeses_eaten = 0
all_cheeses_found = False
mouse_trapped = False

while not all_cheeses_found and not mouse_trapped:
    direction = input()
    if direction == "danger":
        if cheeses_eaten < total_cheeses:
            print("Mouse will come back later!")
        break

    move_row, move_col = possible_directions[direction]
    mouse_row, mouse_col = mouse_coordinates
    new_row = move_row + mouse_row
    new_col = move_col + mouse_col

    if 0 <= new_row < cupboard_rows and 0 <= new_col < cupboard_columns:
        if cupboard[new_row][new_col] == "@":
            continue
        mouse_coordinates = [new_row, new_col]
        cupboard[mouse_row][mouse_col] = "*"

        if cupboard[new_row][new_col] == "C":
            cheeses_eaten += 1
            if cheeses_eaten == total_cheeses:
                all_cheeses_found = True
                print("Happy mouse! All the cheese is eaten, good night!")

        elif cupboard[new_row][new_col] == "T":
            mouse_trapped = True
            print("Mouse is trapped!")

        cupboard[new_row][new_col] = "M"

    else:
        print("No more cheese for tonight!")
        break

[print("".join(row)) for row in cupboard]
