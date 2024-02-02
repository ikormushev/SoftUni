def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget.\n"

    products = {}
    max_products = 5

    for (product, info) in kwargs.items():
        product_price = info[0] * info[1]
        if budget - product_price >= 0:
            budget -= product_price
            products[product] = product_price
            max_products -= 1

            if max_products == 0:
                break

    string_to_print = ""

    for (product_name, total_price) in products.items():
        string_to_print += f"You bought {product_name} for {total_price:.2f} leva.\n"

    return string_to_print


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))

print(shopping_list(20, jeans=(19.99, 1), ))

print(shopping_list(104, cola=(1.20, 2), candies=(0.25, 15), bread=(1.80, 1), pie=(10.50, 5),
                    tomatoes=(4.20, 1), milk=(2.50, 2), juice=(2, 3), eggs=(3, 1), ))
