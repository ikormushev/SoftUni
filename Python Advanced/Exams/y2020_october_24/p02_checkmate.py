from collections import deque

queen_moves = {
    "top": [-1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "down": [1, 0],
    "top-left": [-1, -1],
    "top-right": [-1, 1],
    "down-left": [1, -1],
    "down-right": [1, 1],
}
chess_board_size = 8
board = []
queens_positions = deque()

for row in range(chess_board_size):
    given_row = input().split()
    board.append([])
    for col in range(chess_board_size):
        if given_row[col] == "Q":
            queens_positions.append([row, col])
        board[row].append(given_row[col])

successful_queens = []

while queens_positions:
    queen_row, queen_col = queens_positions.popleft()
    king_reached = False

    for (move, move_info) in queen_moves.items():
        if king_reached:
            break

        move_row, move_col = move_info
        iterations = 0

        for _ in range(chess_board_size):
            if "top" in move:
                move_row -= iterations
            elif "down" in move:
                move_row += iterations

            if "left" in move:
                move_col -= iterations
            elif "right" in move:
                move_col += iterations

            if iterations == 0:
                iterations = 1

            new_row = queen_row + move_row
            new_col = queen_col + move_col

            if 0 <= new_row < chess_board_size and 0 <= new_col < chess_board_size:
                if board[new_row][new_col] == "Q":
                    break
                elif board[new_row][new_col] == "K":
                    king_reached = True
                    successful_queens.append([queen_row, queen_col])
                    break
            else:
                break

if successful_queens:
    [print(x) for x in successful_queens]
else:
    print("The king is safe!")
