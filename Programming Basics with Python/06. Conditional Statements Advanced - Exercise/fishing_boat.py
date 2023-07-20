budget = int(input())
season = input()
fishermen_number = int(input())

price = 0
discount = 0
bigger_discount = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
    bigger_discount = False
elif season == "Winter":
    price = 2600

if fishermen_number <= 6:
    discount = price * 0.10
elif 7 <= fishermen_number <= 11:
    discount = price * 0.15
if fishermen_number >= 12:
    discount = price * 0.25

price -= discount

if not season == "Autumn" and fishermen_number % 2 == 0:
    bigger_discount = price * 0.05
    price -= bigger_discount

money_left = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_left:.2f} leva.")
