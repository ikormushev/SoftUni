from math import floor

money_needed = float(input())
fantasy_books = int(input())
horror_books = int(input())
romantic_books = int(input())

fantasy = fantasy_books * 14.90
horror = horror_books * 9.80
romantic = romantic_books * 4.30

earnings = fantasy + horror + romantic
earnings *= 0.80

money_diff = abs(money_needed - earnings)

if earnings >= money_needed:
    money_per_person = floor(money_diff * 0.10)
    money_left = money_diff - money_per_person
    money_needed += money_left
    print(f"{money_needed:.2f} leva donated.")
    print(f"Sellers will receive {money_per_person} leva.")
else:
    print(f"{money_diff:.2f} money needed.")
