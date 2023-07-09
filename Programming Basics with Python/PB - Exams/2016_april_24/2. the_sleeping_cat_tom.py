num_rest_days = int(input())

playing_norm_minutes_per_year = 30000
playing_while_working_minutes = 63
playing_while_resting_minutes = 127

work_days = 365 - num_rest_days
playing_while_working = work_days * playing_while_working_minutes
playing_while_resting = num_rest_days * playing_while_resting_minutes
play_time = playing_while_working + playing_while_resting

minutes_for_sleeping_left = playing_norm_minutes_per_year - play_time

if play_time > playing_norm_minutes_per_year:
    more_minutes_playing = play_time - playing_norm_minutes_per_year
    only_hours_playing = more_minutes_playing // 60
    only_minutes_playing = more_minutes_playing % 60 # % 60 - взима само остатъка, като така остават минутите;
    print("Tom will run away")
    print(f"{only_hours_playing} hours and {only_minutes_playing} minutes more for play")
else:
    only_hours_for_sleeping = minutes_for_sleeping_left // 60
    only_minutes_for_sleeping = minutes_for_sleeping_left % 60 # % 60 - взима само остатъка, като така остават минутите;
    print("Tom sleeps well")
    print(f"{only_hours_for_sleeping} hours and {only_minutes_for_sleeping} minutes less for play")
