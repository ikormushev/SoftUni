items = input().split("|")
budget = float(input())

train_ticket_price = 150
profit = 0
budget_left = budget
items_bought = []

for i in range(len(items)):
    new_item = items[i].split("->")
    if new_item[0] == "Clothes":
        if float(new_item[1]) > 50.00:
            continue
        budget_left -= float(new_item[1])
    elif new_item[0] == "Shoes":
        if float(new_item[1]) > 35.00:
            continue
        budget_left -= float(new_item[1])
    elif new_item[0] == "Accessories":
        if float(new_item[1]) > 20.50:
            continue
        budget_left -= float(new_item[1])

    if budget_left < 0:
        budget_left += float(new_item[1])
        continue

    items_bought.append(float(new_item[1]))

for y in range(len(items_bought)):
    item_increased_price = items_bought[y] * 1.40
    print(f"{item_increased_price:.2f}", end=" ")
    profit += (item_increased_price - items_bought[y])
    budget_left += item_increased_price
print()
print(f"Profit: {profit:.2f}")
if budget_left >= train_ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")
