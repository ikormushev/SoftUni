starting_time_h = int(input())
arriving_time_h = int(input())
arriving_time_m = int(input())
day_of_week = input()

starting_time_m = starting_time_h * 60
ending_time_m = starting_time_m + (4 * 60)
total_arriving_time_m = (arriving_time_h * 60 + arriving_time_m)

bonus_points = 0

if (starting_time_m - 60) <= total_arriving_time_m < starting_time_m:
    bonus_points += 1.5
elif starting_time_m <= total_arriving_time_m <= (starting_time_m + 30):
    bonus_points += 1
elif (starting_time_m + 30) < total_arriving_time_m <= ending_time_m:
    bonus_points += 0.5

if day_of_week in ["Monday", "Wednesday", "Friday"]:
    bonus_points += 0.6
elif day_of_week in ["Tuesday", "Thursday", "Saturday"]:
    bonus_points += 0.8
elif day_of_week == "Sunday":
    bonus_points += 2

print(f"{bonus_points:.2f}")
