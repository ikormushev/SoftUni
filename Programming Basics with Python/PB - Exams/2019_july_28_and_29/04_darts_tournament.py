starting_points = int(input())

moves = 0

while True:
    sector = input()
    moves += 1
    if sector == "bullseye":
        print(f"Congratulations! You won the game with a bullseye in {moves} moves!")
        break
    points = int(input())

    if sector == "double ring":
        points *= 2
    elif sector == "triple ring":
        points *= 3

    starting_points -= points

    if starting_points == 0:
        print(f"Congratulations! You won the game in {moves} moves!")
        break
    elif starting_points < 0:
        print(f"Sorry, you lost. Score difference: {abs(starting_points)}.")
        break
