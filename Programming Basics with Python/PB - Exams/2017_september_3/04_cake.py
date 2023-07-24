cake_width = int(input())
cake_length = int(input())

cake_area = cake_width * cake_length
taken_pieces = 0
cake_pieces = 0
pieces_left = 0

for _ in range(cake_area):
    cake_pieces = input()
    if cake_pieces == "STOP":
        break
    cake_pieces = int(cake_pieces)
    taken_pieces += cake_pieces
    pieces_left = cake_area - taken_pieces
    if pieces_left < 0:
        pieces_left = abs(pieces_left)
        print(f"No more cake left! You need {pieces_left} pieces more.")
        break

if cake_pieces == "STOP" and pieces_left >= 0:
    print(f"{pieces_left} pieces are left.")
