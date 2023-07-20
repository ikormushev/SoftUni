days = int(input())
room_type = input()
opinion = input()

nights = days - 1
price = 0
discount = 0

if room_type == "room for one person":
    price = nights * 18.00
elif room_type == "apartment":
    price = nights * 25.00
elif room_type == "president apartment":
    price = nights * 35.00

if days < 10:
    if room_type == "apartment":
        discount = price * 0.30
    elif room_type == "president apartment":
        discount = price * 0.10
elif 10 <= days <= 15:
    if room_type == "apartment":
        discount = price * 0.35
    elif room_type == "president apartment":
        discount = price * 0.15
elif days > 15:
    if room_type == "apartment":
        discount = price * 0.50
    elif room_type == "president apartment":
        discount = price * 0.20

price -= discount

opinion_money = 0

if opinion == "positive":
    opinion_money = price * 0.25
    price += opinion_money
elif opinion == "negative":
    opinion_money = price * 0.10
    price -= opinion_money

print(f"{price:.2f}")
