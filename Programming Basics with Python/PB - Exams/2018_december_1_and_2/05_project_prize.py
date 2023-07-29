project_parts = int(input())
prize = float(input())

total_points = 0

for i in range(1, project_parts + 1):
    points = int(input())
    if i % 2 == 0:
        points *= 2
    total_points += points

final_prize = total_points * prize

print(f"The project prize was {final_prize:.2f} lv.")
