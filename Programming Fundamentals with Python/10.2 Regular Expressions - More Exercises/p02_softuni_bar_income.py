import re

pattern = (r"%(?P<name>[A-Z][a-z]+)%[^%\|\$\.]*"
           r"<(?P<product>[\w\-]+)>[^%\|\$\.]*"
           r"\|(?P<count>\d+)\|[^%\|\$\.]*"
           r"(?P<price>(?<=\D)(?:[0-9]|[1-9]\d+)(?:\.\d+)?)\$")

total_income = 0

while True:
    command = input()
    if command == "end of shift":
        print(f"Total income: {total_income:.2f}")
        break
    if re.search(pattern, command):
        customer_info = (re.search(pattern, command)).groupdict()
        customer_name = customer_info["name"]
        product_name = customer_info["product"]
        product_count = int(customer_info["count"])
        product_price = float(customer_info["price"])

        product_total_price = product_count * product_price
        total_income += product_total_price
        print(f"{customer_name}: {product_name} - {product_total_price:.2f}")
