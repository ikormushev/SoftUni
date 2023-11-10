import re

word_pattern = (r"(\@|\#)(?P<first_word>[a-zA-Z]{3,})"
                r"\1{2}(?P<second_word>[a-zA-Z]{3,})\1")

text = input()
valid_words = []

if not re.findall(word_pattern, text):
    print(f"No word pairs found!")
else:
    valid_words = re.finditer(word_pattern, text)
    words_count = len(re.findall(word_pattern, text))
    print(f"{words_count} word pairs found!")
word_matches = []

for pair in valid_words:
    word_pair = pair.groupdict()
    first_word = word_pair["first_word"]
    second_word = word_pair["second_word"]
    if first_word[::-1] == second_word:
        word_matches.append(f"{first_word} <=> {second_word}")

if not word_matches:
    print("No mirror words!")
else:
    print("The mirror words are:")
    for i in range(len(word_matches)):
        if i == len(word_matches) - 1:
            print(word_matches[i])
        else:
            print(word_matches[i], end=", ")
