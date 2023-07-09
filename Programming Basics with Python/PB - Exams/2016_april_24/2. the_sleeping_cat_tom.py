num_rest_days = int(input())

playing_norm_minutes_per_year = 30000
playing_while_working_minutes = 63
playing_while_resting_minutes = 127

work_days = 365 - num_rest_days
playing_while_working = work_days * playing_while_working_minutes
playing_while_resting = num_rest_days * playing_while_resting_minutes
play_time = playing_while_working + playing_while_resting

minutes_difference = abs(playing_norm_minutes_per_year - play_time)
only_hours = minutes_difference // 60
only_minutes = minutes_difference % 60 # % 60 - взима само остатъка, като така остават минутите;

if play_time > playing_norm_minutes_per_year:
    print("Tom will run away")
    print(f"{only_hours} hours and {only_minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{only_hours} hours and {only_minutes} minutes less for play")
