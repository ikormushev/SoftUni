territory_size = int(input())
possible_movements = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

territory = []
alice_coordinates = []

for row in range(territory_size):
    given_row = input().split()
    territory.append([])
    for col in range(territory_size):
        if given_row[col] == "A":
            alice_coordinates = [row, col]
        territory[row].append(given_row[col])

teabags_count = 0
unsuccessful_path = False

while teabags_count < 10 and not unsuccessful_path:
    movement = input()
    current_row, current_col = alice_coordinates
    move_row, move_col = possible_movements[movement]
    new_row = current_row + move_row
    new_col = current_col + move_col
    if 0 <= new_row < territory_size and 0 <= new_col < territory_size:
        element = territory[new_row][new_col]
        if element == "R":
            unsuccessful_path = True
        elif element.isnumeric():
            teabags_count += int(element)
        territory[current_row][current_col] = "*"
        alice_coordinates = [new_row, new_col]
    else:
        unsuccessful_path = True

territory[alice_coordinates[0]][alice_coordinates[1]] = "*"

if unsuccessful_path:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

[print(" ".join(x)) for x in territory]
