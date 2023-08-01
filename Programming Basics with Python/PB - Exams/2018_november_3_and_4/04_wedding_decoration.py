budget = float(input())

products_prices = {
    "balloons": 0.1,
    "flowers": 1.5,
    "candles": 0.5,
    "ribbon": 2
}
products = {
    "balloons": 0,
    "flowers": 0,
    "candles": 0,
    "ribbon": 0
}

total_price = 0

while True:
    command = input()
    if command == "stop":
        money_left = budget - total_price
        print(f"Spend money: {total_price:.2f}")
        print(f"Money left: {money_left:.2f}")
        break
    product_type = command
    product_num = int(input())
    products[product_type] += product_num

    product_price = products_prices[product_type] * product_num
    total_price += product_price

    if budget <= total_price:
        print(f"ALL money is spent!")
        break

print(f"Purchased decoration is {products['balloons']} balloons, "
      f"{products['ribbon']} m ribbon, {products['flowers']} flowers "
      f"and {products['candles']} candles.")
