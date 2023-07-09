film_budget = float(input())
extras_num = int(input())
extra_clothes_price = float(input())

decor_price = film_budget * 0.1

if extras_num > 150:
    extra_clothes_price = extra_clothes_price - extra_clothes_price * 0.1

extras_price = extras_num * extra_clothes_price
film_price = extras_price + decor_price
money_difference = abs(film_price - film_budget)

if film_price > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {money_difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_difference:.2f} leva left.")
