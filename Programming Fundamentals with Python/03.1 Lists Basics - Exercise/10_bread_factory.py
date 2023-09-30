working_day_events = input().split("|")

initial_energy = 100
current_energy = initial_energy

initial_coins = 100
current_coins = initial_coins

for i in range(len(working_day_events)):
    event_info = working_day_events[i].split("-")
    gained_energy = 0
    coins_earned = 0
    coins_spent = 0

    if event_info[0] == "rest":
        current_energy += int(event_info[1])
        if current_energy >= initial_energy:
            current_energy -= int(event_info[1])
            gained_energy = initial_energy - current_energy
            current_energy += gained_energy
        else:
            gained_energy = int(event_info[1])
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")
    elif event_info[0] == "order":
        coins_earned += int(event_info[1])
        current_energy -= 30
        if current_energy >= 0:
            current_coins += coins_earned
            print(f"You earned {coins_earned} coins.")
        else:
            # by condition, you skip the order which means you get the 30 energy back on top of the 50 bonus
            current_energy += 50 + 30
            print("You had to rest!")
    else:
        coins_spent = int(event_info[1])
        current_coins -= coins_spent
        if current_coins >= 0:
            print(f"You bought {event_info[0]}.")
        else:
            current_coins += coins_spent
            print(f"Closed! Cannot afford {event_info[0]}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {current_coins}")
    print(f"Energy: {current_energy}")
