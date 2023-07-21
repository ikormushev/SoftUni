season = input()
km_per_month = float(input())

earnings = 0

if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        earnings = km_per_month * 0.75
    elif season == "Summer":
        earnings = km_per_month * 0.90
    elif season == "Winter":
        earnings = km_per_month * 1.05
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        earnings = km_per_month * 0.95
    elif season == "Summer":
        earnings = km_per_month * 1.10
    elif season == "Winter":
        earnings = km_per_month * 1.25
elif 10000 < km_per_month <= 20000:
    earnings = km_per_month * 1.45

earnings *= 4
taxes = earnings * 0.10
earnings -= taxes

print(f"{earnings:.2f}")
