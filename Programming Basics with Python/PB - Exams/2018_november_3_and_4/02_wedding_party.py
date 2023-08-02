guests_num = int(input())
budget = int(input())

total_coverts = guests_num * 20
money_diff = abs(budget - total_coverts)

if budget >= total_coverts:
    fireworks = money_diff * 0.40
    donation = money_diff * 0.60
    print(f"Yes! {fireworks:.0f} lv are for fireworks "
          f"and {donation:.0f} lv are for donation.")
else:
    print(f"They won't have enough money to pay the covert. "
          f"They will need {money_diff:.0f} lv more.")
