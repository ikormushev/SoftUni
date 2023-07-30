amount = float(input())

total_coins = 0

amount_left = float(f"{amount * 100:.2f}")  # if we do not format the number, we could encounter errors

while amount_left != 0:
    if amount_left >= 200:
        amount_left -= 200
    elif amount_left >= 100:
        amount_left -= 100
    elif amount_left >= 50:
        amount_left -= 50
    elif amount_left >= 20:
        amount_left -= 20
    elif amount_left >= 10:
        amount_left -= 10
    elif amount_left >= 5:
        amount_left -= 5
    elif amount_left >= 2:
        amount_left -= 2
    elif amount_left >= 1:
        amount_left -= 1
    total_coins += 1

print(total_coins)
