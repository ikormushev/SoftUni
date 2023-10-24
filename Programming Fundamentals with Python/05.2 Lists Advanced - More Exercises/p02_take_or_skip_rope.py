def symbol_checker(letter: str) -> bool:
    if letter.isnumeric():
        return True
    return False


text = input()

numbers_list = [x for x in text if symbol_checker(x)]
non_numbers_list = [x for x in text if not symbol_checker(x)]

take_numbers_list = []
skip_numbers_list = []

for k in range(len(numbers_list)):
    if k % 2 == 0:
        take_numbers_list.append(int(numbers_list[k]))
    else:
        skip_numbers_list.append(int(numbers_list[k]))

symbols = non_numbers_list.copy()
taken_string = ""
index = 0

# by condition, it is said that the number of numbers will always be an even number
for i in range(int(len(numbers_list) / 2)):
    for y in range(take_numbers_list[i]):
        if symbols[0] == "" and len(symbols) == 1:
            break
        taken_string += symbols[y]
        symbols[y] = ""

    for _ in range(symbols.count("")):
        symbols.remove("")

    for z in range(skip_numbers_list[i]):
        if len(symbols) == 0:
            break
        symbols[z] = ""

    for _ in range(symbols.count("")):
        symbols.remove("")

print(taken_string)
