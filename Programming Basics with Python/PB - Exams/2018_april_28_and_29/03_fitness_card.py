budget = float(input())
gender = input()
age = int(input())
sport = input()

sport_prices = {
    "m": {
        "Gym": 42,
        "Boxing": 41,
        "Yoga": 45,
        "Zumba": 34,
        "Dances": 51,
        "Pilates": 39
    },
    "f": {
        "Gym": 35,
        "Boxing": 37,
        "Yoga": 42,
        "Zumba": 31,
        "Dances": 53,
        "Pilates": 37
    }
}

price = sport_prices[gender][sport]

if age <= 19:
    price *= 0.80

if budget >= price:
    print(f"You have purchased a 1 month pass for {sport}.")
else:
    money_diff = price - budget
    print(f"You don't have enough money! You need ${money_diff:.2f} more.")
