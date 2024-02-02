from collections import deque

orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]

total_pizzas = 0

while orders and employees:
    order = orders.popleft()
    if order <= 0 or order > 10:
        continue

    employee = employees.pop()

    if order > employee:
        total_pizzas += employee
        order -= employee
        orders.appendleft(order)
    else:
        total_pizzas += order

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees:", end=" ")
    print(*employees, sep=", ")
elif not employees and orders:
    print("Not all orders are completed.")
    print("Orders left:", end=" ")
    print(*orders, sep=", ")
