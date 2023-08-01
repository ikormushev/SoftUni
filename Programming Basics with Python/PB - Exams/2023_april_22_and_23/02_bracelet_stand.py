daily_pocket_money = float(input())
daily_earnings = float(input())
expenses = float(input())
gift_price = float(input())

total_earnings = daily_earnings * 5
total_pocket_money = daily_pocket_money * 5
money_left = total_pocket_money + total_earnings - expenses

if money_left >= gift_price:
    print(f"Profit: {money_left:.2f} BGN, the gift has been purchased.")
else:
    money_needed = gift_price - money_left
    print(f"Insufficient money: {money_needed:.2f} BGN.")
