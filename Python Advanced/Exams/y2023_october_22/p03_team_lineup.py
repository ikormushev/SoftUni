def team_lineup(*args):
    players_by_country = {}

    for (player_name, country) in args:
        if country not in players_by_country:
            players_by_country[country] = []
        players_by_country[country].append(player_name)

    sorted_players_by_country = dict(sorted(players_by_country.items(), key=lambda d: (-len(d[1]), d[0])))

    string_to_print = ""
    for (country, players) in sorted_players_by_country.items():
        string_to_print += f"{country}:\n"
        for player in players:
            string_to_print += f"  -{player}\n"

    return string_to_print


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
