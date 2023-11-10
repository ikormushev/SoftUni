import re

pattern = r"w{3}\.[a-zA-Z0-9\-]+(?:\.[a-z]+){1,}"

while True:
    command = input()
    if command == "":
        break
    valid_links = re.finditer(pattern, command)
    for link in valid_links:
        print(link.group())
