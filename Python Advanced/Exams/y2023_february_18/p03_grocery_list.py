def shop_from_grocery_list(budget, products, *args):
    purchased_items = {}
    for (product_name, price) in args:
        if product_name in products:
            if product_name not in purchased_items:
                if budget - price >= 0:
                    purchased_items[product_name] = price
                    budget -= price
                else:
                    break
    missing_products = []
    for product in products:
        if product not in purchased_items.keys():
            missing_products.append(product)

    string_to_return = ""
    if not missing_products:
        string_to_return = f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        string_to_return = (f"You did not buy all the products. "
                            f"Missing products: {', '.join(missing_products)}.")

    return string_to_return


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
