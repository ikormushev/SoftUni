product = input()
product_count = int(input())

products_prices = {
    "coffee": 1.50,
    "water": 1.00,
    "coke": 1.40,
    "snacks": 2.00
}


def product_price(x, y):
    total_price = x * y
    return total_price


print(f"{product_price(products_prices[product], product_count):.2f}")
