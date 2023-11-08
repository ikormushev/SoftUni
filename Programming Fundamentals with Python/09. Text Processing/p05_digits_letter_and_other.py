random_strings = list(input())

digits = ""
letters = ""
others = ""

for symbol in random_strings:
    if symbol.isnumeric():
        digits += symbol
    elif ord(symbol) in range(ord("a"), ord("z") + 1) or ord(symbol) in range(ord("A"), ord("Z") + 1):
        letters += symbol
    else:
        others += symbol

print(digits)
print(letters)
print(others)
