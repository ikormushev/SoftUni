dancers_num = int(input())
points = float(input())
season = input()
place = input()

prize = 0
season_expenses = 0

if place == "Bulgaria":
    prize = points * dancers_num
    if season == "summer":
        season_expenses = prize * 0.05
    elif season == "winter":
        season_expenses = prize * 0.08
elif place == "Abroad":
    prize = (points * dancers_num) * 1.50
    if season == "summer":
        season_expenses = prize * 0.10
    elif season == "winter":
        season_expenses = prize * 0.15

prize -= season_expenses
charity_money = prize * 0.75
money_per_dancer = (prize * 0.25) / dancers_num

print(f"Charity - {charity_money:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
