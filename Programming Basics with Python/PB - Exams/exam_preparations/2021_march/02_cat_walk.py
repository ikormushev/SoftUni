daily_walk_min = int(input())
daily_walks_num = int(input())
calorie_intake = int(input())

total_walks_min = daily_walk_min * daily_walks_num
calorie_deficit = total_walks_min * 5

if calorie_deficit >= (calorie_intake * 0.50):
    print(f"Yes, the walk for your cat is enough. "
          f"Burned calories per day: {calorie_deficit}.")
else:
    print(f"No, the walk for your cat is not enough. "
          f"Burned calories per day: {calorie_deficit}.")
