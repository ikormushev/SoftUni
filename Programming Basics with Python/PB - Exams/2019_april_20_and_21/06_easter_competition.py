breads_num = int(input())

winner_points = 0
baker_name = ""
winner_name = 0

for _ in range(1, breads_num + 1):
    baker_name = input()
    baker_points = 0
    is_winner = False
    while True:
        command = input()

        if command == "Stop":
            if baker_points > winner_points:
                is_winner = True
                winner_name = baker_name
                winner_points = baker_points
            print(f"{baker_name} has {baker_points} points.")
            if is_winner:
                print(f"{baker_name} is the new number 1!")
            break

        bread_points = int(command)
        baker_points += bread_points

print(f"{winner_name} won competition with {winner_points} points!")
