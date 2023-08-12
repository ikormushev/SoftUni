stage = input()
ticket_type = input()
tickets_num = int(input())
photo = input()

prices = {
    "Standard": {
        "Quarter final": 55.50,
        "Semi final": 75.88,
        "Final": 110.10
    },
    "Premium": {
        "Quarter final": 105.20,
        "Semi final": 125.22,
        "Final": 160.66
    },
    "VIP": {
        "Quarter final": 118.90,
        "Semi final": 300.40,
        "Final": 400
    }
}

photo_price = 0
if photo == "Y":
    photo_price = 40

price = prices[ticket_type][stage] * tickets_num

if price > 4000:
    photo_price = 0
    price *= 0.75
elif price > 2500:
    price *= 0.90

price += photo_price * tickets_num

print(f"{price:.2f}")
