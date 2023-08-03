budget = float(input())
nights = int(input())
night_price = float(input())
extra_expenses_percentage = int(input()) / 100

if nights > 7:
    night_price *= 0.95

price = nights * night_price
extra_expenses = budget * extra_expenses_percentage
price += extra_expenses

money_diff = abs(price - budget)
if budget >= price:
    print(f"Ivanovi will be left with {money_diff:.2f} "
          f"leva after vacation.")
else:
    print(f"{money_diff:.2f} leva needed.")
