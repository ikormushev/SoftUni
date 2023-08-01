team = input()
souvenir = input()
souvenirs_num = int(input())

teams_list = ["Argentina", "Brazil", "Croatia", "Denmark"]
souvenirs_list = ["flags", "caps", "posters", "stickers"]

souvenir_prices = {
    "flags": {
        "Argentina": 3.25,
        "Brazil": 4.20,
        "Croatia": 2.75,
        "Denmark": 3.10
    },
    "caps": {
        "Argentina": 7.20,
        "Brazil": 8.50,
        "Croatia": 6.90,
        "Denmark": 6.50
    },
    "posters": {
        "Argentina": 5.10,
        "Brazil": 5.35,
        "Croatia": 4.95,
        "Denmark": 4.80
    },
    "stickers": {
        "Argentina": 1.25,
        "Brazil": 1.20,
        "Croatia": 1.10,
        "Denmark": 0.90
    }
}

if team not in teams_list:
    print("Invalid country!")
elif souvenir not in souvenirs_list:
    print("Invalid stock!")
else:
    price = souvenirs_num * souvenir_prices[souvenir][team]
    print(f"Pepi bought {souvenirs_num} {souvenir} of {team} for {price:.2f} lv.")
