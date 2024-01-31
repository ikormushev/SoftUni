import os
import re

words_dict = {}
word_pattern = r"[a-zA-z]+(?:['-][a-zA-z]+)*"

word_file_path = os.path.join("files_used", "words.txt")
with open(word_file_path, "r") as words_file:
    words = [x.lower() for line in words_file.readlines() for x in line.split()]

input_file_path = os.path.join("files_used", "input.txt")
with open(input_file_path, "r") as input_file:
    words_found = [x.lower() for line in input_file.readlines() for x in re.findall(word_pattern, line)]

for word in words:
    if word not in words_dict:
        words_dict[word] = 0

for word in words_found:
    if word in words_dict:
        words_dict[word] += 1

sorted_dict = dict(sorted(words_dict.items(), key=lambda d: -d[1]))

output_file_path = os.path.join("files_used", "output.txt")
with open(output_file_path, "w") as output_file:
    for (word, frequency) in sorted_dict.items():
        output_file.write(f"{word} - {frequency}\n")
