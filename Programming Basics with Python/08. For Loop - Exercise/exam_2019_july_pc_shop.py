games_sold = int(input())

g1, g2, g3, g4 = 0, 0, 0, 0  # "Hearthstone", "Fornite", "Overwatch", "Others"

for _ in range(games_sold):
    game_name = input()
    if game_name == "Hearthstone":
        g1 += 1
    elif game_name == "Fornite":
        g2 += 1
    elif game_name == "Overwatch":
        g3 += 1
    else:
        g4 += 1

g1_percent = g1 / games_sold * 100
g2_percent = g2 / games_sold * 100
g3_percent = g3 / games_sold * 100
g4_percent = g4 / games_sold * 100

print(f"Hearthstone - {g1_percent:.2f}%")
print(f"Fornite - {g2_percent:.2f}%")
print(f"Overwatch - {g3_percent:.2f}%")
print(f"Others - {g4_percent:.2f}%")
