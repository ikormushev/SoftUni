games_sold = int(input())

games_list = ["Hearthstone", "Fornite", "Overwatch"]

games_numbers = {
    "Hearthstone": 0,
    "Fornite": 0,
    "Overwatch": 0,
    "Others": 0
}

for _ in range(1, games_sold + 1):
    game_name = input()
    if game_name in games_list:
        games_numbers[game_name] += 1
    else:
        games_numbers["Others"] += 1

hearthstone_percent = games_numbers["Hearthstone"] / games_sold * 100
fornite_percent = games_numbers["Fornite"] / games_sold * 100
overwatch_percent = games_numbers["Overwatch"] / games_sold * 100
others_percent = games_numbers["Others"] / games_sold * 100

print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")
