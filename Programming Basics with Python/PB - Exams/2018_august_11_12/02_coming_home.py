distance_km = int(input())
petrol_per_100_km = int(input())
petrol_price_lt = float(input())
earnings = int(input())

car_expense_lt = distance_km * petrol_per_100_km / 100
price = car_expense_lt * petrol_price_lt
money_left = earnings - price

earnings_per_person = earnings / 5

if price <= earnings:
    print(f"You can go home. {money_left:.2f} money left.")
else:
    print(f"Sorry, you cannot go home. Each will receive {money_left:.2f} money.")
