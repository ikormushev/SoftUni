def are_coordinates_valid(row, col):
    if 0 <= row < rows_num and 0 <= col < columns_num:
        if board[row][col] == "." and not visited_spots[row][col]:
            return True
    return False


# Using Depth First Search (DFS) algorithm to find the connections
def find_connections(row, col):
    if not are_coordinates_valid(row, col):
        return 0

    visited_spots[row][col] = True
    current_connections = 1

    for connection in possible_connections:
        con_row, con_col = possible_connections[connection]
        new_row = con_row + row
        new_col = con_col + col
        current_connections += find_connections(new_row, new_col)

    return current_connections


def largest_connection():
    max_connections = 0
    for i in range(rows_num):
        for j in range(columns_num):
            if board[i][j] == "." and not visited_spots[i][j]:
                count = find_connections(i, j)
                max_connections = max(max_connections, count)
    return max_connections


possible_connections = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

rows_num = int(input())

board = [input().split() for _ in range(rows_num)]
columns_num = len(board[0])
visited_spots = [[False for _ in range(columns_num)] for _ in range(rows_num)]
current_max_connections = 0

print(largest_connection())
