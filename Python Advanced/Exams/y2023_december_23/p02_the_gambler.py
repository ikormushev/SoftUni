possible_directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

matrix_size = int(input())

matrix = []
gambler_position = []

for row in range(matrix_size):
    given_row = input()
    matrix.append([])
    for col in range(matrix_size):
        if given_row[col] == "G":
            gambler_position = [row, col]
        matrix[row].append(given_row[col])

initial_entering_game = 100
jackpot_won = False
gambler_lost = False

while True:
    command = input()
    if command == "end":
        break

    direction_row, direction_col = possible_directions[command]
    current_row, current_col = gambler_position

    new_row = direction_row + current_row
    new_col = direction_col + current_col
    matrix[current_row][current_col] = "-"

    if 0 <= new_row < matrix_size and 0 <= new_col < matrix_size:
        current_element = matrix[new_row][new_col]
        if current_element == "W":
            initial_entering_game += 100
        elif current_element == "P":
            initial_entering_game -= 200
        elif current_element == "J":
            initial_entering_game += 100000
            matrix[new_row][new_col] = "G"
            jackpot_won = True
            break

        if initial_entering_game <= 0:
            gambler_lost = True
            break

        matrix[new_row][new_col] = "G"
        gambler_position = [new_row, new_col]
    else:
        gambler_lost = True
        break

if gambler_lost:
    print("Game over! You lost everything!")
else:
    if jackpot_won:
        print("You win the Jackpot!")
    print(f"End of the game. Total amount: {initial_entering_game}$")

if initial_entering_game > 0:
    [print("".join(row)) for row in matrix]
