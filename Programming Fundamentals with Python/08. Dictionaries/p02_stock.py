stock_elements = input().split(" ")
searched_products = input().split(" ")

stock = {}

for i in range(0, len(stock_elements), 2):
    product = stock_elements[i]
    quantities = stock_elements[i + 1]
    stock[product] = quantities

for y in range(len(searched_products)):
    wanted_product = searched_products[y]
    if wanted_product in stock:
        print(f"We have {stock[wanted_product]} of {wanted_product} left")
    else:
        print(f"Sorry, we don't have {wanted_product}")
