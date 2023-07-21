chrysanthemums_num = int(input())
roses_num = int(input())
tulips_num = int(input())
season = input()
holiday = input()

flowers_num = chrysanthemums_num + roses_num + tulips_num
price = 0

if season == "Spring" or season == "Summer":
    price = (chrysanthemums_num * 2.00) + (roses_num * 4.10) + (tulips_num * 2.50)
elif season == "Autumn" or season == "Winter":
    price = (chrysanthemums_num * 3.75) + (roses_num * 4.50) + (tulips_num * 4.15)

if holiday == "Y":
    price = price * 1.15

if tulips_num > 7 and season == "Spring":
    price = price * 0.95
elif roses_num >= 10 and season == "Winter":
    price = price * 0.90

if flowers_num > 20:
    price = price * 0.80

making_bouquet = 2

price = price + 2

print(f"{price:.2f}")
