destination = input()
march_dates = input()
nights = int(input())

prices = {
    "21-23": {
        "France": 30,
        "Italy": 28,
        "Germany": 32
    },
    "24-27": {
        "France": 35,
        "Italy": 32,
        "Germany": 37
    },
    "28-31": {
        "France": 40,
        "Italy": 39,
        "Germany": 43
    },
}

price = prices[march_dates][destination] * nights

print(f"Easter trip to {destination} : {price:.2f} leva.")
