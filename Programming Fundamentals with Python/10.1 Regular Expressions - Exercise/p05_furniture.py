import re

# valid pattern for Judge
furniture_pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(?:.[0-9]+)?)!(?P<quantity>\d+)"
# this pattern does not exclude the case when the price is starting with a zero (09, 01, etc.)

furniture_cost = 0
furniture = []

while True:
    command = input()
    if command == "Purchase":
        break
    if re.search(furniture_pattern, command):
        furniture_info = (re.search(furniture_pattern, command)).groupdict()
        furniture_name = furniture_info["name"]
        furniture_price = float(furniture_info["price"])
        furniture_quantity = int(furniture_info["quantity"])

        furniture.append(furniture_name)
        furniture_cost += furniture_price * furniture_quantity

print("Bought furniture:")
[print(x) for x in furniture]
print(f"Total money spend: {furniture_cost:.2f}")
