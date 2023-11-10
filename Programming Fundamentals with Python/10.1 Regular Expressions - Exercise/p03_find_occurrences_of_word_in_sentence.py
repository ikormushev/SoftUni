import re

text = input().lower()
wanted_word = input().lower()
pattern = fr"\b{wanted_word}\b"

word_count = len(re.findall(pattern, text))
print(word_count)
