import re

calories_pattern = r"(\||\#)(?:[a-zA-Z ]+)\1(?:\d{2,}\/\d{2,}\/\d{2,})\1(?P<calories>\d+)\1"

pattern = (r"(\||\#)(?P<name>[a-zA-Z ]+)\1"
           r"(?P<expiration>\d{2,}\/\d{2,}\/\d{2,})\1"
           r"(?P<calories>\d+)\1")
text = input()

daily_calories = 2000
total_calories = 0

calories = re.finditer(calories_pattern, text)

for cal in calories:
    total_calories += int(cal.groupdict()["calories"])

total_days = total_calories // daily_calories
print(f"You have food to last you for: {total_days} days!")
valid_products = re.finditer(pattern, text)

for new_product in valid_products:
    product_info = new_product.groupdict()
    print(f'Item: {product_info["name"]}, '
          f'Best before: {product_info["expiration"]}, '
          f'Nutrition: {product_info["calories"]}')
