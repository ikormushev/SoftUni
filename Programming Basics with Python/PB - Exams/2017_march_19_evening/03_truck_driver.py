season = input()
km_per_month = float(input())

earnings_km_to_5000 = {
    "Spring": 0.75,
    "Summer": 0.90,
    "Autumn": 0.75,
    "Winter": 1.05
}

earnings_km_to_10000 = {
    "Spring": 0.95,
    "Summer": 1.10,
    "Autumn": 0.95,
    "Winter": 1.25
}

earnings = 0

if km_per_month <= 5000:
    earnings = (km_per_month * earnings_km_to_5000[season]) * 4
elif 5000 < km_per_month <= 10000:
    earnings = (km_per_month * earnings_km_to_10000[season]) * 4
elif 10000 < km_per_month <= 20000:
    earnings = (km_per_month * 1.45) * 4

earnings *= 0.9

print(f"{earnings:.2f}")
