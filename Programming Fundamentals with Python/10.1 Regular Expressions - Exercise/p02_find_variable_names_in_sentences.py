import re

names_pattern = r"(?<=\b_{1})[a-zA-Z0-9]+\b"
variable_names = input()

valid_names = re.findall(names_pattern, variable_names)
print(*valid_names, sep=",")
