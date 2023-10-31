products = {}

while True:
    command = input()
    if command == "statistics":
        break
    pair = command.split(": ")
    if pair[0] in products:
        products[pair[0]] += int(pair[1])
    else:
        products[pair[0]] = int(pair[1])

print("Products in stock:")

for product, quality in products.items():
    print(f"- {product}: {quality}")

print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
