from math import ceil
series = input()
episode_time = int(input())
lunch_break_time = int(input())

lunch_time = lunch_break_time * 1/8
rest_time = lunch_break_time * 1/4

final_time = episode_time + lunch_time + rest_time
time_difference = ceil(abs(lunch_break_time - final_time))

if final_time <= lunch_break_time:
    print(f"You have enough time to watch {series} and left with {time_difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {time_difference} more minutes.")
