import re

regex_pattern = r"\D+\d+"
sequence = re.findall(regex_pattern, input())

symbols_used = []
rage_message = ""

for i in range(len(sequence)):
    wanted_string = ""
    string_repetition = 0
    for y in range(len(sequence[i])):
        symbol = sequence[i][y]
        if symbol.isnumeric():
            string_repetition = int(sequence[i][y:])
            break
        else:
            wanted_string += symbol.upper()
            if symbol.upper() not in symbols_used:
                symbols_used.append(symbol.upper())
    wanted_string *= string_repetition
    rage_message += wanted_string

print(f"Unique symbols used: {len(symbols_used)}")
print(rage_message)
