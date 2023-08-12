actor_name = input()
starting_points = float(input())
judges_num = int(input())

points = starting_points
enough_points = False

for _ in range(1, judges_num + 1):
    judge_name = input()
    judge_points = float(input())
    points += (len(judge_name) * judge_points) / 2

    if points >= 1250.5:
        enough_points = True
        break

if enough_points:
    print(f"Congratulations, {actor_name} got a nominee "
          f"for leading role with {points:.1f}!")
else:
    points_diff = 1250.5 - points
    print(f"Sorry, {actor_name} you need {points_diff:.1f} more!")
