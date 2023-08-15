
total_wins_ally = 0
total_wins_enemy = 0

while True:
    command = input()
    if command == "End of tournaments":
        break
    tournament_name = command
    tournament_matches = int(input())

    for m in range(1, tournament_matches + 1):
        points_ally = int(input())
        points_enemy = int(input())

        points_diff = abs(points_ally - points_enemy)
        if points_ally > points_enemy:
            total_wins_ally += 1
            print(f"Game {m} of tournament {tournament_name}: win with {points_diff} points.")
        else:
            total_wins_enemy += 1
            print(f"Game {m} of tournament {tournament_name}: lost with {points_diff} points.")

total_matches = total_wins_ally + total_wins_enemy
wins_percentage = total_wins_ally / total_matches * 100
losses_percentage = total_wins_enemy / total_matches * 100

print(f"{wins_percentage:.2f}% matches win")
print(f"{losses_percentage:.2f}% matches lost")
