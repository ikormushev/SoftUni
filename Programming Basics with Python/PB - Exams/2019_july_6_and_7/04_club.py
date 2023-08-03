wanted_earnings = float(input())

total_earnings = 0

while True:
    command = input()
    if command == "Party!":
        money_needed = wanted_earnings - total_earnings
        print(f"We need {money_needed:.2f} leva more.")
        break
    cocktail_name = command
    cocktails_num = int(input())

    cocktail_price = len(cocktail_name)
    order = cocktails_num * cocktail_price
    if order % 2 == 1:
        order *= 0.75
    total_earnings += order

    if total_earnings >= wanted_earnings:
        print("Target acquired.")
        break

print(f"Club income - {total_earnings:.2f} leva.")
