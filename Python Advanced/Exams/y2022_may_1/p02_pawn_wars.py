from collections import deque


def position_on_board(board_row, board_col):
    board_row = board_size - board_row
    board_col = chr(ord("a") + board_col)
    return f"{board_col}{board_row}"


board_size = 8
players = deque(["white", "black"])

player_info = {
    "white": {
        "movement": [-1, 0],
        "diagonal_move": [[-1, -1], [-1, 1]],
        "current_position": [],
        "enemy": "b"
    },
    "black": {
        "movement": [1, 0],
        "diagonal_move": [[1, -1], [1, 1]],
        "current_position": [],
        "enemy": "w"
    }
}

board = []
for row in range(board_size):
    given_row = input().split()
    board.append([])
    for col in range(board_size):
        if given_row[col] == "w":
            player_info["white"]["current_position"] = [row, col]
        elif given_row[col] == "b":
            player_info["black"]["current_position"] = [row, col]
        board[row].append(given_row[col])

player_win = False

while True:
    current_player = players.popleft()
    players.append(current_player)
    current_row, current_col = player_info[current_player]["current_position"]
    new_row, new_col = 0, 0

    for possible_attack in player_info[current_player]["diagonal_move"]:
        move_row, move_col = possible_attack
        new_row = move_row + current_row
        new_col = move_col + current_col
        if 0 <= new_row < board_size and 0 <= new_col < board_size:
            if board[new_row][new_col] == player_info[current_player]["enemy"]:
                board[new_row][new_col] = current_player[0]
                player_win = True
                break

    if player_win:
        current_player = current_player[0].capitalize() + current_player[1:]
        square = position_on_board(new_row, new_col)
        print(f"Game over! {current_player} win, capture on {square}.")
        break

    move_row, move_col = player_info[current_player]["movement"]
    new_row = move_row + current_row
    new_col = move_col + current_col
    if 0 <= new_row < board_size and 0 <= new_col < board_size:
        board[current_row][current_col] = "-"
        board[new_row][new_col] = current_player[0]
        player_info[current_player]["current_position"] = [new_row, new_col]

        current_square = position_on_board(new_row, new_col)
        current_player = current_player[0].capitalize() + current_player[1:]
        if current_player == "White" and new_row == 0:
            print(f"Game over! {current_player} pawn is promoted to a queen at {current_square}.")
            break
        elif current_player == "Black" and new_row == board_size - 1:
            print(f"Game over! {current_player} pawn is promoted to a queen at {current_square}.")
            break
