actor_name = input()
points = float(input())
raters_num = int(input())

for _ in range(raters_num):
    rater_name = input()
    points_rater = float(input())
    points += (len(rater_name) * points_rater) / 2
    if points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee "
              f"for leading role with {points}!")
        break
else:
    points_diff = 1250.5 - points
    print(f"Sorry, {actor_name} you need {points_diff} more!")
