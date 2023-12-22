import re

pattern = r"(.+)>(?P<numbers>[0-9]{3})\|(?P<lowercase>[a-z]{3})\|(?P<uppercase>[A-Z]{3})\|(?P<other>[^<>]{3})<\1$"

inputs_count = int(input())

for _ in range(inputs_count):
    password = input()
    if re.search(pattern, password):
        password_groups = re.search(pattern, password).groupdict()
        new_password = (password_groups["numbers"] + password_groups["lowercase"]
                        + password_groups["uppercase"] + password_groups["other"])
        print(f"Password: {new_password}")
    else:
        print("Try another password!")
