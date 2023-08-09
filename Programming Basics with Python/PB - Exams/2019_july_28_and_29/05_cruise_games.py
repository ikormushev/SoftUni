from math import floor

player_name = input()
games_played = int(input())

games_difficulty = {
    "volleyball": 0.07,
    "tennis": 0.05,
    "badminton": 0.02
}

games_num = {
    "volleyball": 0,
    "tennis": 0,
    "badminton": 0
}

games_points = {
    "volleyball": 0,
    "tennis": 0,
    "badminton": 0
}

points_total = 0

for i in range(1, games_played + 1):
    game_name = input()
    points = int(input())
    points *= 1 + games_difficulty[game_name]

    games_points[game_name] += points
    points_total += points
    games_num[game_name] += 1

if ((games_points["volleyball"] // games_num["volleyball"]) >= 75
        and (games_points["tennis"] // games_num["tennis"]) >= 75
        and (games_points["badminton"] // games_num["badminton"]) >= 75):
    print(f"Congratulations, {player_name}! You won the cruise "
          f"games with {floor(points_total)} points.")
else:
    print(f"Sorry, {player_name}, you lost. Your points are only {floor(points_total)}.")
