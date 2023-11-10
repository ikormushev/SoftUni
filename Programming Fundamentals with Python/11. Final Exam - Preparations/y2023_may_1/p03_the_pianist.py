pieces_num = int(input())

pieces = {}

for _ in range(pieces_num):
    info = input().split("|")
    piece = info[0]
    composer = info[1]
    key = info[2]
    pieces[piece] = {}
    pieces[piece]["composer"] = composer
    pieces[piece]["key"] = key

while True:
    command = input()
    if command == "Stop":
        break
    action = command.split("|")
    piece = action[1]
    non_existent_piece = False

    if action[0] == "Add":
        composer = action[2]
        key = action[3]
        if piece not in pieces:
            pieces[piece] = {}
            pieces[piece]["composer"] = composer
            pieces[piece]["key"] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action[0] == "Remove":
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            non_existent_piece = True

    elif action[0] == "ChangeKey":
        new_key = action[2]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            non_existent_piece = True

    if non_existent_piece:
        print(f"Invalid operation! {piece} does not exist in the collection.")

for (one_piece, info) in pieces.items():
    print(f'{one_piece} -> Composer: {pieces[one_piece]["composer"]}, Key: {pieces[one_piece]["key"]}')
