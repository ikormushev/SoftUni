lines_num = int(input())

symbols_list = []

for _ in range(1, lines_num + 1):
    text_line = input()

    if text_line == "(" or text_line == ")":
        symbols_list.append(text_line)

previous_line = ""
times_balanced = 0
for y in range(len(symbols_list)):
    if y == 0 or y % 2 == 0:
        previous_line = symbols_list[y]
        continue

    if previous_line == "(" and symbols_list[y] == ")":
        times_balanced += 1

if times_balanced == len(symbols_list) / 2:
    print("BALANCED")
else:
    print("UNBALANCED")
