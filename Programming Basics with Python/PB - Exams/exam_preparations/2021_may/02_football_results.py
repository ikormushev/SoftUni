first_match = input()
second_match = input()
third_match = input()

games_won = 0
games_lost = 0
games_draw = 0

if int(first_match[0]) > int(first_match[2]):
    games_won += 1
elif int(first_match[0]) == int(first_match[2]):
    games_draw += 1
else:
    games_lost += 1

if int(second_match[0]) > int(second_match[2]):
    games_won += 1
elif int(second_match[0]) == int(second_match[2]):
    games_draw += 1
else:
    games_lost += 1

if int(third_match[0]) > int(third_match[2]):
    games_won += 1
elif int(third_match[0]) == int(third_match[2]):
    games_draw += 1
else:
    games_lost += 1

print(f"Team won {games_won} games.")
print(f"Team lost {games_lost} games.")
print(f"Drawn games: {games_draw}")
