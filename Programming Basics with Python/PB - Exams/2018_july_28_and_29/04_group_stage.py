team_name = input()
matches_played = int(input())

points = 0
goals_in_total = 0
goals_received_total = 0

for _ in range(1, matches_played + 1):
    goals_in = int(input())
    goals_received = int(input())
    if goals_in > goals_received:
        points += 3
    elif goals_in == goals_received:
        points += 1
    goals_in_total += goals_in
    goals_received_total += goals_received

goal_difference = goals_in_total - goals_received_total

if goals_in_total >= goals_received_total:
    print(f"{team_name} has finished the group phase with {points} points.")
    print(f"Goal difference: {goal_difference}.")
else:
    print(f"{team_name} has been eliminated from the group phase.")
    print(f"Goal difference: {goal_difference}.")
