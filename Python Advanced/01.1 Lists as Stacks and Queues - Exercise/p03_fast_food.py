from collections import deque

daily_food = int(input())
food_quantity_per_order = deque([int(x) for x in input().split()])
print(max(food_quantity_per_order))

while food_quantity_per_order:
    current_order = food_quantity_per_order.popleft()
    if daily_food - current_order >= 0:
        daily_food -= current_order
    else:
        print(f"Orders left: {current_order}", *food_quantity_per_order)
        break
else:
    print("Orders complete")
