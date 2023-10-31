bakery_elements = input().split(" ")

bakery = {}

for i in range(0, len(bakery_elements), 2):
    food = bakery_elements[i]
    quantities = bakery_elements[i + 1]
    bakery[food] = int(quantities)

print(bakery)
