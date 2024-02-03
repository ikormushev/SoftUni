from collections import deque


def calculating_sum(row, col):
    total_sum = 0
    for (move, position) in numbers_per_col_row.items():
        if move in ["left", "right"]:
            count_row, count_col = position(row)
        else:
            count_row, count_col = position(col)
        total_sum += int(matrix[count_row][count_col])

    return total_sum


players = deque(input().split(", "))
players_info = {}

for _ in range(len(players)):
    player = players.popleft()
    players_info[player] = {}
    players_info[player]["points"] = 501
    players_info[player]["turns"] = 0
    players.append(player)

numbers_per_col_row = {
    "left": lambda x: [x, 0],
    "top": lambda x: [0, x],
    "right": lambda x: [x, -1],
    "down": lambda x: [-1, x]
}

matrix_size = 7
matrix = [input().split() for _ in range(matrix_size)]

while True:
    current_player = players.popleft()
    players.append(current_player)
    players_info[current_player]["turns"] += 1

    hit = input().split(", ")
    hit_row = int(hit[0][1:])
    hit_col = int(hit[1][:-1])

    if 0 <= hit_row < matrix_size and 0 <= hit_col < matrix_size:
        current_element = matrix[hit_row][hit_col]
        if current_element.isnumeric():
            players_info[current_player]["points"] -= int(current_element)
        elif current_element == "D":
            players_info[current_player]["points"] -= calculating_sum(hit_row, hit_col) * 2
        elif current_element == "T":
            players_info[current_player]["points"] -= calculating_sum(hit_row, hit_col) * 3
        elif current_element == "B":
            print(f"{current_player} won the game with {players_info[current_player]['turns']} throws!")
            break

        if players_info[current_player]["points"] <= 0:
            print(f"{current_player} won the game with {players_info[current_player]['turns']} throws!")
            break
