egg_size = input()
egg_paint = input()
eggs_num = int(input())

prices = {
    "Large": {
        "Red": 16,
        "Green": 12,
        "Yellow": 9
    },
    "Medium": {
        "Red": 13,
        "Green": 9,
        "Yellow": 7
    },
    "Small": {
        "Red": 9,
        "Green": 8,
        "Yellow": 5
    }
}

price = eggs_num * prices[egg_size][egg_paint]

price *= 0.65

print(f"{price:.2f} leva.")
