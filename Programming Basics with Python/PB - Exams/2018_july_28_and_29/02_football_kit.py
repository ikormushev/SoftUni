shirt_price = float(input())
money_needed_ball = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (shirt_price + shorts_price) * 2

final_price = shirt_price + shorts_price + socks_price + shoes_price
final_price *= 0.85

if final_price >= money_needed_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {final_price:.2f} lv.")
else:
    money_diff = money_needed_ball - final_price
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {money_diff:.2f} lv. more.")
