cruise_type = input()
cabin_type = input()
nights = int(input())

prices = {
    "standard cabin": {
        "Mediterranean": 27.50,
        "Adriatic": 22.99,
        "Aegean": 23.00
    },
    "cabin with balcony": {
        "Mediterranean": 30.20,
        "Adriatic": 25.00,
        "Aegean": 26.60
    },
    "apartment": {
        "Mediterranean": 40.50,
        "Adriatic": 34.99,
        "Aegean": 39.80
    }
}

price = prices[cabin_type][cruise_type] * 4 * nights

if nights > 7:
    price *= 0.75

print(f"Annie's holiday in the {cruise_type} sea costs {price:.2f} lv.")
