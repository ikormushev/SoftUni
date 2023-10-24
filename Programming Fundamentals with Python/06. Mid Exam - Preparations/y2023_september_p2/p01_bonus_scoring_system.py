from math import ceil

students_num = int(input())
lectures_num = int(input())
bonus_points = int(input())

max_points = 0
max_attendances = 0
for _ in range(students_num):
    attendances_count = int(input())
    total_bonus = attendances_count / lectures_num * (5 + bonus_points)
    if total_bonus > max_points:
        max_points = total_bonus
        max_attendances = attendances_count

print(f"Max Bonus: {ceil(max_points)}.")
print(f"The student has attended {max_attendances} lectures.")
