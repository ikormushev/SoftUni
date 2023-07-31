team_name = input()
matches_played = int(input())

additional_time = 0
penalties = 0
total_time = 0

for _ in range(1, matches_played + 1):
    game_time = int(input())
    if game_time > 90:
        additional_time += 1
        if game_time > 120:
            additional_time -= 1  # additional_time doesn't count when there are penalties
            penalties += 1
    total_time += game_time

average_time = total_time / matches_played

print(f"{team_name} has played {total_time} minutes. "
      f"Average minutes per game: {average_time:.2f}")
print(f"Games with penalties: {penalties}")
print(f"Games with additional time: {additional_time}")
