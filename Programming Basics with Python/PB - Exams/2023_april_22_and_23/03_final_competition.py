dancers_num = int(input())
points = float(input())
season = input()
place = input()

seasonal_expenses = {
    "summer": {
        "Bulgaria": 0.05,
        "Abroad": 0.10
    },
    "winter": {
        "Bulgaria": 0.08,
        "Abroad": 0.15
    }
}

prize = 0

if place == "Bulgaria":
    prize = points * dancers_num
elif place == "Abroad":
    prize = (points * dancers_num) * 1.50

prize *= 1 - seasonal_expenses[season][place]
charity = prize * 0.75
money_per_dancer = (prize * 0.25) / dancers_num

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
