from collections import deque

field_size = 6
possible_moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

field = []
rover_coordinates = []

for row in range(field_size):
    given_row = input().split()
    field.append([])
    for col in range(field_size):
        if given_row[col] == "E":
            rover_coordinates = [row, col]
        field[row].append(given_row[col])

all_moves = deque(input().split(", "))

deposits = {
    "W": {"count": 0, "name": "Water"},
    "M": {"count": 0, "name": "Metal"},
    "C": {"count": 0, "name": "Concrete"}
}

while all_moves:
    current_move = all_moves.popleft()
    move_row, move_col = possible_moves[current_move]
    rover_row, rover_col = rover_coordinates
    new_row = move_row + rover_row
    new_col = move_col + rover_col
    if not (0 <= new_row < field_size) or not (0 <= new_col < field_size):
        if new_row < 0:
            new_row = field_size - 1
        elif new_row >= field_size:
            new_row = 0

        if new_col < 0:
            new_col = field_size - 1
        elif new_col >= field_size:
            new_col = 0

    current_element = field[new_row][new_col]
    if current_element in deposits:
        deposits[current_element]['count'] += 1
        print(f"{deposits[current_element]['name']} deposit found at ({new_row}, {new_col})")
    elif current_element == "R":
        print(f"Rover got broken at ({new_row}, {new_col})")
        break
    rover_coordinates = [new_row, new_col]

one_of_each = True

for (deposit, info) in deposits.items():
    if info["count"] < 1:
        one_of_each = False

if one_of_each:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
