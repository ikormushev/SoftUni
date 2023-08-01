command = input()

best_player = ""
most_goals = 0
is_hat_trick = False

while command != "END":
    player_name = command
    goals_num = int(input())
    if goals_num > most_goals:
        best_player = player_name
        most_goals = goals_num
    if most_goals >= 10:
        break
    command = input()
if most_goals >= 3:
    is_hat_trick = True

print(f"{best_player} is the best player!")
if is_hat_trick:
    print(f"{best_player} has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"{best_player} has scored {most_goals} goals.")
