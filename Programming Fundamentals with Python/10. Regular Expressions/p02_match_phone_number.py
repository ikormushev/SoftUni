import re

numbers = input()

number_pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
valid_numbers = re.findall(number_pattern, numbers)
print(*valid_numbers, sep=", ")
