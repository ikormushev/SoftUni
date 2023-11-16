import re

names_pattern = r" *, *"
valid_name_pattern = r"^[^ ,]+$"
health_pattern = r"[^0-9\+\-\*\/\.]"
damage_pattern = r"[\+\-]?\d+(?:\.\d+)?"
names = re.split(names_pattern, input())

demons = {}

for name in names:
    if re.search(valid_name_pattern, name) is None:
        continue
    demon_health_symbols = re.findall(health_pattern, name)
    demon_health_symbols_codes = [ord(x) for x in demon_health_symbols]
    demon_health = sum(demon_health_symbols_codes)

    demon_damage_ticks = re.findall(damage_pattern, name)
    demon_damage_numbers = []
    for tick in demon_damage_ticks:
        number = 0
        if tick[0] == "-":
            number = -float(tick[1:])
        elif tick[0] == "+":
            number = float(tick[1:])
        else:
            number = float(tick)
        demon_damage_numbers.append(number)
    demon_damage = sum(demon_damage_numbers)

    for i in range(len(name)):
        if name[i] == "*":
            demon_damage *= 2
        elif name[i] == "/":
            demon_damage /= 2

    demons[name] = {}
    demons[name]["health"] = demon_health
    demons[name]["damage"] = demon_damage

sorted_demons = dict(sorted(demons.items()))

for (demon, stats) in sorted_demons.items():
    print(f'{demon} - {stats["health"]} health, {stats["damage"]:.2f} damage')
