from collections import deque

ramen_bowls = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while ramen_bowls and customers:
    ramen_bowl = ramen_bowls.pop()
    customer = customers.popleft()

    if ramen_bowl > customer:
        ramen_bowl -= customer
        ramen_bowls.append(ramen_bowl)
    elif ramen_bowl < customer:
        customer -= ramen_bowl
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if ramen_bowls:
        print("Bowls of ramen left:", end=" ")
        print(*ramen_bowls, sep=", ")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print("Customers left:", end=" ")
    print(*customers, sep=", ")
