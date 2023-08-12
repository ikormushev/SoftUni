wanted_earnings = float(input())

earnings = 0

while True:
    command = input()
    if command == "Party!":
        money_needed = wanted_earnings - earnings
        print(f"We need {money_needed:.2f} leva more.")
        break
    cocktail_name = command
    cocktails_num = int(input())
    price = len(cocktail_name) * cocktails_num
    if price % 2 == 1:
        price *= 0.75
    earnings += price

    if earnings >= wanted_earnings:
        print("Target acquired.")
        break

print(f"Club income - {earnings:.2f} leva.")
