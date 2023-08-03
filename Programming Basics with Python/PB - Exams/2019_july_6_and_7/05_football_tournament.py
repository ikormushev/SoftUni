team_name = input()
games_played = int(input())

results = {
    "W": 0,
    "D": 0,
    "L": 0
}

points = {
    "W": 3,
    "D": 1,
    "L": 0
}

total_points = 0

if games_played == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    for _ in range(games_played):
        game_result = input()
        results[game_result] += 1
        total_points += points[game_result]

    games_won_percentage = results["W"] / games_played * 100

    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f'## W: {results["W"]}')
    print(f'## D: {results["D"]}')
    print(f'## L: {results["L"]}')
    print(f"Win rate: {games_won_percentage:.2f}%")
