project_parts = int(input())
money_prize_per_point = float(input())

points_total = 0

for i in range(1, project_parts + 1):
    points = int(input())
    if i % 2 == 0:
        points *= 2
    points_total += points

project_prize = points_total * money_prize_per_point

print(f"The project prize was {project_prize:.2f} lv.")
