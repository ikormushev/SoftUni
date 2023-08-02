daily_walk_m = int(input())
daily_walks_num = int(input())
daily_calories = int(input())

total_walks_min = daily_walk_m * daily_walks_num
calories_burned = total_walks_min * 5

enough_calories = daily_calories * 0.50

if calories_burned >= enough_calories:
    print(f"Yes, the walk for your cat is enough. "
          f"Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. "
          f"Burned calories per day: {calories_burned}.")
