players = {}

while True:
    command = input()
    if command == "Season end":
        break

    if "->" in command:
        action = command.split(" -> ")
        player = action[0]
        position = action[1]
        skill = int(action[2])

        if player not in players:
            players[player] = {}
            players[player][position] = skill
        else:
            if position not in players[player]:
                players[player][position] = skill
            else:
                if skill > players[player][position]:
                    players[player][position] = skill

    else:
        action = command.split(" vs ")
        first_player = action[0]
        second_player = action[1]
        if first_player in players and second_player in players:
            position_in_common = False
            first_player_positions = dict(players[first_player])
            second_player_positions = dict(players[second_player])

            for searched_position in first_player_positions.keys():
                if searched_position in second_player_positions.keys():
                    position_in_common = True

            if position_in_common and not ((first_player_positions.keys() == second_player_positions.keys())
                                           and (sum(first_player_positions.values())
                                                == sum(second_player_positions.values()))):
                if sum(first_player_positions.values()) > sum(second_player_positions.values()):
                    del players[second_player]
                elif sum(second_player_positions.values()) > sum(first_player_positions.values()):
                    del players[first_player]

ordered_players = dict(sorted(players.items(), key=lambda d: (-sum(d[1].values()), d[0])))

for (wanted_player, positions) in ordered_players.items():
    print(f"{wanted_player}: {sum(positions.values())} skill")
    positions = dict(sorted(positions.items(), key=lambda d: (-d[1], d[0])))
    for (wanted_position, wanted_skill) in positions.items():
        print(f"- {wanted_position} <::> {wanted_skill}")