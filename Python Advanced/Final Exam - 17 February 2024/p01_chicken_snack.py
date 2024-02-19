from collections import deque

amounts_of_money = [int(x) for x in input().split()]
food_prices = deque([int(x) for x in input().split()])

food_count = 0

while amounts_of_money and food_prices:
    amount = amounts_of_money.pop()
    price = food_prices.popleft()

    if amount >= price:
        food_count += 1
        if amount > price:
            amount -= price
            if amounts_of_money:
                next_amount = amounts_of_money.pop()
                next_amount += amount
                amounts_of_money.append(next_amount)
            else:
                amounts_of_money.append(amount)

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif 1 < food_count < 4:
    print(f"Henry ate: {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
