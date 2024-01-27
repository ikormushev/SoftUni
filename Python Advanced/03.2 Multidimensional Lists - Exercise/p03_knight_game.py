from collections import deque

board_size = int(input())
board = [list(input()) for _ in range(board_size)]

knight_moves = {
    "top left": [-1, -2],
    "next top left": [-2, -1],
    "top right": [-2, 1],
    "next top right": [-1, 2],
    "bot right": [1, 2],
    "next bot right": [2, 1],
    "bot left": [2, -1],
    "next bot left": [1, -2]
}

knights = deque()
knights_removed = 0

for row in range(board_size):
    for col in range(board_size):
        if board[row][col] == "K":
            knights.append([row, col])

while True:
    max_knights_hit = 0
    strongest_knight = []
    knights_left = []

    while knights:
        knight_row, knight_col = knights.popleft()
        if board[knight_row][knight_col] == 0:
            continue
        total_knights_hit = 0
        for move, position in knight_moves.items():
            move_row, move_col = position
            next_row = knight_row + move_row
            next_col = knight_col + move_col
            if 0 <= next_row < board_size and 0 <= next_col < board_size:
                if board[next_row][next_col] == "K":
                    total_knights_hit += 1
        if total_knights_hit > max_knights_hit:
            max_knights_hit = total_knights_hit
            strongest_knight = [knight_row, knight_col]

        knights_left.append([knight_row, knight_col])

    if strongest_knight:
        knights_left.remove(strongest_knight)
        knights = deque(knights_left)

        knight_row, knight_col = strongest_knight
        knights_removed += 1
        board[knight_row][knight_col] = 0
    else:
        break


print(knights_removed)
