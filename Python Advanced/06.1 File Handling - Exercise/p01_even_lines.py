import os

symbols_to_replace = ["-", ",", ".", "!", "?"]

file_path = os.path.join("files_used", "text.txt")
with open(file_path) as file:
    file_text = file.readlines()

for i in range(len(file_text)):
    if i % 2 == 1:
        continue

    line = file_text[i]
    line_to_print = ''.join(line[:-1])

    for symbol in symbols_to_replace:
        if symbol in line_to_print:
            line_to_print = line_to_print.replace(symbol, "@")

    line_to_print = line_to_print.split()
    print(" ".join(line_to_print[::-1]))
