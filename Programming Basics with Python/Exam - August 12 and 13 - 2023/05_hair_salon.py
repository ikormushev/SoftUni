daily_goal = int(input())

prices = {
    "haircut": {
        "mens": 15,
        "ladies": 20,
        "kids": 10
    },
    "color": {
        "touch up": 20,
        "full color": 30
    },
}

total_daily_earnings = 0
is_goal_reached = False

while True:
    command = input()
    if command == "closed":
        break
    service_type = input()
    earnings = prices[command][service_type]
    total_daily_earnings += earnings

    if total_daily_earnings >= daily_goal:
        is_goal_reached = True
        break

if is_goal_reached:
    print("You have reached your target for the day!")
else:
    money_needed = daily_goal - total_daily_earnings
    print(f"Target not reached! You need {money_needed}lv. more.")

print(f"Earned money: {total_daily_earnings}lv.")
