products = {}

while True:
    command = input()
    if command == "buy":
        break
    product_info = command.split(" ")
    product_name = product_info[0]
    product_price = float(product_info[1])
    product_quantity = int(product_info[2])

    if product_name not in products:
        products[product_name] = {}
        products[product_name]["price"] = product_price
        products[product_name]["quantity"] = product_quantity
    else:
        products[product_name]["quantity"] += product_quantity
        if products[product_name]["price"] != product_price:
            products[product_name]["price"] = product_price

[print(f'{name} -> {info["price"] * info["quantity"]:.2f}') for (name, info) in products.items()]
