shirt_price = float(input())
money_needed = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = 2 * (shirt_price + shorts_price)

total_price = shirt_price + shorts_price + socks_price + shoes_price
total_price *= 0.85

if total_price >= money_needed:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    money_diff = money_needed - total_price
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {money_diff:.2f} lv. more.")
