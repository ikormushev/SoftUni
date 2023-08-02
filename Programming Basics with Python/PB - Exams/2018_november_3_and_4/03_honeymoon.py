budget = float(input())
city = input()
nights_num = int(input())

prices = {
    "nights": {  # prices per person
        "Cairo": 250,
        "Paris": 150,
        "Lima": 400,
        "New York": 300,
        "Tokyo": 350
    },
    "tickets": {  # prices for both of them
        "Cairo": 600,
        "Paris": 350,
        "Lima": 850,
        "New York": 650,
        "Tokyo": 750
    }
}

final_price = (prices["nights"][city] * nights_num) * 2 + prices["tickets"][city]

discount = 0
if 1 <= nights_num <= 4:
    if city in ["Cairo", "New York"]:
        discount = 0.03
elif 5 <= nights_num <= 9:
    if city in ["Cairo", "New York"]:
        discount = 0.05
    elif city == "Paris":
        discount = 0.07
elif 10 <= nights_num <= 24:
    if city in ["New York", "Paris", "Tokyo"]:
        discount = 0.12
    elif city == "Cairo":
        discount = 0.10
elif 25 <= nights_num <= 49:
    if city in ["Cairo", "Tokyo"]:
        discount = 0.17
    elif city in ["New York", "Lima"]:
        discount = 0.19
    elif city == "Paris":
        discount = 0.22
elif nights_num >= 50:
    discount = 0.30

final_price *= 1 - discount
money_diff = abs(budget - final_price)

if budget >= final_price:
    print(f"Yes! You have {money_diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {money_diff:.2f} leva.")
