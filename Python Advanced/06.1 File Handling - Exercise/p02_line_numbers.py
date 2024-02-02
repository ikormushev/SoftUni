import os

lines = {}
punctuation_marks = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
input_file_path = os.path.join("files_used", "text.txt")

with open(input_file_path) as input_file:
    file_text = input_file.readlines()

for i in range(1, len(file_text) + 1):
    line = file_text[i-1]
    if line[-1] == "\n":
        line = line[:-1]

    lines[i] = {}
    lines[i]["line"] = line
    lines[i]["letters"], lines[i]["punctuation"] = 0, 0

    for symbol in lines[i]["line"]:
        if symbol.isalpha():
            lines[i]["letters"] += 1
        elif symbol in punctuation_marks:
            lines[i]["punctuation"] += 1

output_file_path = os.path.join("files_used", "output.txt")
with open(output_file_path, "w") as output_file:
    for (line_num, line_info) in lines.items():
        line_to_write = (f"Line {line_num}: {line_info['line']} "
                         f"({line_info['letters']})({line_info['punctuation']})\n")
        output_file.write(line_to_write)
