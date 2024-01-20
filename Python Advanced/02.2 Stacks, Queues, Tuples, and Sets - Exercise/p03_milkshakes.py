from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque([int(x) for x in input().split(", ")])

total_milkshakes = 0

while chocolates and milk_cups and total_milkshakes < 5:
    chocolate = chocolates.pop()
    milk_cup = milk_cups.popleft()
    if chocolate <= 0 or milk_cup <= 0:
        if chocolate <= 0 < milk_cup:
            milk_cups.appendleft(milk_cup)
        if milk_cup <= 0 < chocolate:
            chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        total_milkshakes += 1
    else:
        milk_cups.append(milk_cup)
        chocolate -= 5
        chocolates.append(chocolate)

if total_milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print("Chocolate: ", end="")
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")

if milk_cups:
    print("Milk: ", end="")
    print(*milk_cups, sep=", ")
else:
    print("Milk: empty")
