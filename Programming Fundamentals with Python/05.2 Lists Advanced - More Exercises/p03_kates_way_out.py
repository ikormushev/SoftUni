def are_coordinates_valid(row, col):
    if 0 <= row < rows_count and 0 <= col < columns_count:
        return True
    return False


def kates_position(given_matrix):
    for row in range(rows_count):
        for col in range(len(given_matrix[row])):
            if given_matrix[row][col] == "k":
                return [row, col]


def explore_maze(matrix, current_moves=0):
    global current_max_moves
    while True:
        current_position = kates_position(matrix)

        if current_position is None:
            if current_max_moves <= 0:
                return "Kate cannot get out"
            else:
                return current_max_moves
        kate_row, kate_col = current_position
        visited_cells = [kate_row, kate_col]
        matrix[kate_row][kate_col] = "."

        for move in possible_moves:
            move_row, move_col = possible_moves[move]
            new_row = move_row + kate_row
            new_col = move_col + kate_col

            if are_coordinates_valid(new_row, new_col) and [new_row, new_col] not in visited_cells:
                if maze[new_row][new_col] == " ":
                    maze[new_row][new_col] = "k"
                    explore_maze(matrix, current_moves + 1)
            else:
                current_moves += 1
                if current_moves > current_max_moves:
                    current_max_moves = current_moves
                current_moves -= 1  # just works


possible_moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
rows_count = int(input())
maze = [list(input()) for _ in range(rows_count)]
columns_count = len(maze[0])

current_max_moves = 0
visited_cells = []

max_moves = explore_maze(maze)

if isinstance(max_moves, int):
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")
