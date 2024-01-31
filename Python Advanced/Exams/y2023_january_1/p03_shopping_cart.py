def shopping_cart(*args):
    cart = {
        "Soup": {
            "limit": 3,
            "products": []
        },
        "Pizza": {
            "limit": 4,
            "products": []
        },
        "Dessert": {
            "limit": 2,
            "products": []
        }
    }

    for info in args:
        if info == "Stop":
            break
        meal, product = info
        if len(cart[meal]["products"]) < cart[meal]["limit"]:
            if product not in cart[meal]["products"]:
                cart[meal]["products"].append(product)

    sorted_cart = dict(sorted(cart.items(), key=lambda d: (-len(d[1]["products"]), d[0])))
    string_to_print = ""
    if not [product for x in sorted_cart.items() for product in x[1]["products"]]:
        string_to_print = "No products in the cart!"
    else:
        for (meal, info) in sorted_cart.items():
            string_to_print += f"{meal}:\n"
            sorted_products = sorted(info["products"])
            for product in sorted_products:
                string_to_print += f" - {product}\n"

    return string_to_print
