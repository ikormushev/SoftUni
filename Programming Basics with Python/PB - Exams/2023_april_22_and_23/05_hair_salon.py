target = int(input())
command = input()

prices = {
    "haircut": {
        "mens": 15,
        "ladies": 20,
        "kids": 10
    },
    "color": {
        "touch up": 20,
        "full color": 30
    }
}

earnings = 0

while command != "closed":
    if command == "haircut":
        haircut_type = input()
        price = prices[command][haircut_type]
        earnings += price
    elif command == "color":
        color_type = input()
        price = prices[command][color_type]
        earnings += price
    if earnings >= target:
        break
    command = input()

if earnings >= target:
    print("You have reached your target for the day!")
else:
    money_needed = target - earnings
    print(f"Target not reached! You need {money_needed}lv. more.")
print(f"Earned money: {earnings}lv.")
