words_count = int(input())

words = {}

for _ in range(words_count):
    word = input()
    synonym = input()
    if word not in words:
        words[word] = synonym
    else:
        words[word] += f", {synonym}"

[print(f"{w} - {s}") for (w, s) in words.items()]
