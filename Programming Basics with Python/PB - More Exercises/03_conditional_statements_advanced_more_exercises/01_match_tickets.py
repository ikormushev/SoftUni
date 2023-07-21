budget = float(input())
category = input()
people_number = int(input())

ticket = 0
transport_price = 0

if category == "VIP":
    ticket = 499.99
elif category == "Normal":
    ticket = 249.99

if 1 <= people_number <= 4:
    transport_price = budget * 0.75
elif 5 <= people_number <= 9:
    transport_price = budget * 0.60
elif 10 <= people_number <= 24:
    transport_price = budget * 0.50
elif 25 <= people_number <= 49:
    transport_price = budget * 0.40
elif people_number >= 50:
    transport_price = budget * 0.25

budget -= transport_price
tickets_price = ticket * people_number
money_diff = abs(budget - tickets_price)

if budget >= tickets_price:
    print(f"Yes! You have {money_diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_diff:.2f} leva.")
