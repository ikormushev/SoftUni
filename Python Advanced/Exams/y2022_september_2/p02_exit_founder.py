from collections import deque

players = deque(input().split(", "))

matrix_size = 6
matrix = [input().split() for _ in range(matrix_size)]

players_trapped = {}  # Not hardcoded to be Tom/Jerry -> loop needed to fill the dict

for _ in range(len(players)):
    current_player = players.popleft()
    players_trapped[current_player] = False
    players.append(current_player)

while True:
    current_player = players.popleft()
    players.append(current_player)

    current_coordinates = input().split(", ")
    current_row = int(current_coordinates[0][1:])
    current_col = int(current_coordinates[1][:-1])

    if players_trapped[current_player]:
        players_trapped[current_player] = False
        continue

    if matrix[current_row][current_col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[current_row][current_col] == "T":
        winner = players.popleft()
        print(f"{current_player} is out of the game! The winner is {winner}.")
        break
    elif matrix[current_row][current_col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        players_trapped[current_player] = True
