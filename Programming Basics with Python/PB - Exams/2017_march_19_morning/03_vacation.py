budget = float(input())
season = input()

price = 0
accommodation = ""
location = ""

accommodation_prices_summer = {
    "Camp": budget * 0.65,
    "Hut": budget * 0.80,
    "Hotel": budget * 0.90
}
accommodation_prices_winter = {
    "Camp": budget * 0.45,
    "Hut": budget * 0.60,
    "Hotel": budget * 0.90
}

if budget <= 1000:
    accommodation = "Camp"
elif 1000 < budget <= 3000:
    accommodation = "Hut"
elif budget > 3000:
    accommodation = "Hotel"

if season == "Summer":
    location = "Alaska"
    price = accommodation_prices_summer[accommodation]
elif season == "Winter":
    location = "Morocco"
    price = accommodation_prices_winter[accommodation]

print(f"{location} - {accommodation} - {price:.2f}")
