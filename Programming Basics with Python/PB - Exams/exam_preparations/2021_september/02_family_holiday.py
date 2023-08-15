budget = float(input())
nights = int(input())
night_price = float(input())
more_expenses_percentage = int(input()) / 100

if nights > 7:
    night_price *= 0.95

price = nights * night_price
total_expenses = price + budget * more_expenses_percentage

money_diff = abs(budget - total_expenses)

if budget >= total_expenses:
    print(f"Ivanovi will be left with {money_diff:.2f} leva after vacation.")
else:
    print(f"{money_diff:.2f} leva needed.")
