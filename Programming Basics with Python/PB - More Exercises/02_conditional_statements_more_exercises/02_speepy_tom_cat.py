rest_days = int(input())

maximum_playing_time_min = 30000
petting_while_working_min = 63
petting_while_resting_min = 127

work_days = 365 - rest_days
real_playtime = (petting_while_working_min * work_days) + \
                (rest_days * petting_while_resting_min)

time_difference = abs(maximum_playing_time_min - real_playtime)
time_difference_h = time_difference // 60
time_difference_min = time_difference % 60

if real_playtime > maximum_playing_time_min:
    print("Tom will run away")
    print(f"{time_difference_h} hours and {time_difference_min} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{time_difference_h} hours and {time_difference_min} minutes less for play")
