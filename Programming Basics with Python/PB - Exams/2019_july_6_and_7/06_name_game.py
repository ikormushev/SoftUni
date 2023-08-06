max_points = 0
max_points_player = ""

while True:
    points = 0
    command = input()
    if command == "Stop":
        print(f"The winner is {max_points_player} with {max_points} points!")
        break
    player_name = command
    for n in range(len(player_name)):
        number = int(input())
        if number == ord(player_name[n]):
            points += 10
        else:
            points += 2
    if points >= max_points:
        max_points_player = player_name
        max_points = points
