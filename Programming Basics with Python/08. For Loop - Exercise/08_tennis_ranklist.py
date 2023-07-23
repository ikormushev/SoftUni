from math import floor

tournaments_num = int(input())
points = int(input())

tournaments_won = 0
points_won = 0

for _ in range(1, tournaments_num + 1):
    tournament_stage = input()
    if tournament_stage == "W":
        tournaments_won += 1
        points_won += 2000
    elif tournament_stage == "F":
        points_won += 1200
    elif tournament_stage == "SF":
        points_won += 720

points += points_won
average_points_won = points_won / tournaments_num
winning_percent = tournaments_won / tournaments_num * 100

print(f"Final points: {points}")
print(f"Average points: " + str(floor(average_points_won)))
print(f"{winning_percent:.2f}%")
