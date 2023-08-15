from math import floor

series_name = input()
seasons_num = int(input())
episodes_num = int(input())
episode_time = float(input())

ad_time = episode_time * 0.20
episode_total_time = ad_time + episode_time

special_episode_time = 10

total_time = seasons_num * (episode_total_time * episodes_num + special_episode_time)

print(f"Total time needed to watch the {series_name} "
      f"series is {floor(total_time)} minutes.")
