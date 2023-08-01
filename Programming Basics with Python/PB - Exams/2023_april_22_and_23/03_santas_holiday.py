days = int(input())
room_type = input()
opinion = input()

nights = days - 1

room_nights_prices = {
    "room for one person": 18.00,
    "apartment": 25.00,
    "president apartment": 35.00
}

discount_less_than_10_days = {
    "room for one person": 0,
    "apartment": 0.30,
    "president apartment": 0.10
}

discount_between_10_15_days = {
    "room for one person": 0,
    "apartment": 0.35,
    "president apartment": 0.15
}

discount_more_than_15_days = {
    "room for one person": 0,
    "apartment": 0.50,
    "president apartment": 0.20
}

price = room_nights_prices[room_type] * nights

if days < 10:
    price *= 1 - discount_less_than_10_days[room_type]
elif 10 <= days <= 15:
    price *= 1 - discount_between_10_15_days[room_type]
elif days > 15:
    price *= 1 - discount_more_than_15_days[room_type]

if opinion == "positive":
    price *= 1.25
elif opinion == "negative":
    price *= 0.90

print(f"{price:.2f}")
