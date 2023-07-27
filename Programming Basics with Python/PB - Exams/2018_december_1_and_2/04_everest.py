height = 5364
days = 1

while True:  # could be done with a for loop with range(1, 6) because the day_cap is 5
    sleeping = input()
    if sleeping == "No":
        days += 0
    elif sleeping == "Yes":
        days += 1
    if sleeping == "END":
        print("Failed!")
        print(f"{height}")
        break
    meters_climbed = int(input())
    if days > 5:
        print("Failed!")
        print(f"{height}")
        break
    height += meters_climbed
    if height >= 8848:
        print(f"Goal reached for {days} days!")
        break
