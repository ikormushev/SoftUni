import re

names_pattern = r"(=|\/)(?P<name>[A-Z][a-zA-Z]{2,})\1"

names = input()
valid_names = re.finditer(names_pattern, names)

travel_points = 0
locations = []

for name in valid_names:
    location = name.groupdict()["name"]
    travel_points += len(location)
    locations.append(location)

print("Destinations: ", end="")
print(*locations, sep=", ")
print(f"Travel Points: {travel_points}")
