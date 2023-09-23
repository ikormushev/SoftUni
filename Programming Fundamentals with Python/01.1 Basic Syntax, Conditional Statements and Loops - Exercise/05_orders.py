orders_num = int(input())

total_price = 0

for _ in range(1, orders_num + 1):
    order_price = float(input())
    days_num = int(input())
    daily_capsules = int(input())

    if (not (0.01 <= order_price <= 100)
            or not (1 <= days_num <= 31)
            or not (1 <= daily_capsules <= 2000)):
        continue

    price = order_price * days_num * daily_capsules
    total_price += price

    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
