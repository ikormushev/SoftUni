import re

pattern = r"\d+"
extracted_numbers = []

while True:
    text = input()
    if text == "":
        break
    numbers = re.findall(pattern, text)
    for number in numbers:
        extracted_numbers.append(number)


print(*extracted_numbers)
