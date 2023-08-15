games_sold = int(input())

games_list = ["Hearthstone", "Fornite", "Overwatch"]

games = {
    "Hearthstone": 0,
    "Fornite": 0,
    "Overwatch": 0,
    "Others": 0
}

for _ in range(1, games_sold + 1):
    game_name = input()
    if game_name in games_list:
        games[game_name] += 1
    else:
        games["Others"] += 1

print(f'Hearthstone - {(games["Hearthstone"] / games_sold * 100):.2f}%')
print(f'Fornite - {(games["Fornite"] / games_sold * 100):.2f}%')
print(f'Overwatch - {(games["Overwatch"] / games_sold * 100):.2f}%')
print(f'Others - {(games["Others"] / games_sold * 100):.2f}%')
