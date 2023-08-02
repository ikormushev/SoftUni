bachelorette_party_price = float(input())
love_letters_num = int(input())
roses_num = int(input())
keychains_num = int(input())
caricatures_num = int(input())
fortunes_num = int(input())

products_total = love_letters_num + roses_num + keychains_num + caricatures_num + fortunes_num

love_letters = love_letters_num * 0.60
roses = roses_num * 7.2
keychains = keychains_num * 3.60
caricatures = caricatures_num * 18.20
fortunes = fortunes_num * 22

earnings = love_letters + roses + keychains + caricatures + fortunes

if products_total >= 25:
    earnings *= 0.65

hosting_price = earnings * 0.10
earnings -= hosting_price

money_diff = abs(earnings - bachelorette_party_price)

if earnings >= bachelorette_party_price:
    print(f"Yes! {money_diff:.2f} lv left.")
else:
    print(f"Not enough money! {money_diff:.2f} lv needed.")
