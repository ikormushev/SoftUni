movie_name = input()
hall_type = input()
tickets_num = int(input())

prices = {
    "normal": {
        "A Star Is Born": 7.50,
        "Bohemian Rhapsody": 7.35,
        "Green Book": 8.15,
        "The Favourite": 8.75
    },
    "luxury": {
        "A Star Is Born": 10.50,
        "Bohemian Rhapsody": 9.45,
        "Green Book": 10.25,
        "The Favourite": 11.55
    },
    "ultra luxury": {
        "A Star Is Born": 13.50,
        "Bohemian Rhapsody": 12.75,
        "Green Book": 13.25,
        "The Favourite": 13.95
    },
}

price = prices[hall_type][movie_name] * tickets_num

print(f"{movie_name} -> {price:.2f} lv.")
