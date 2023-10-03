cards = input().split(" ")

cards_list = list(cards)

first_team_players_count = 11
second_team_players_count = 11
terminated_game = False
seen_players = []

for i in range(len(cards_list)):
    if cards_list[i] in seen_players:
        continue
    seen_players.append(cards_list[i])

    if "A" in cards_list[i]:
        first_team_players_count -= 1
    elif "B" in cards_list[i]:
        second_team_players_count -= 1

    if first_team_players_count < 7 or second_team_players_count < 7:
        terminated_game = True
        break

print(f"Team A - {first_team_players_count}; "
      f"Team B - {second_team_players_count}")
if terminated_game:
    print("Game was terminated")
