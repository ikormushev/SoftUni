import re
numbers_pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
numbers = input()

valid_numbers = re.finditer(numbers_pattern, numbers)

for number in valid_numbers:
    print(number.group(), end=" ")
