words = input().split(" ")

words_count = {}

for i in range(len(words)):
    found_word = words[i].lower()
    if found_word not in words_count:
        words_count[found_word] = 1
    else:
        words_count[found_word] += 1

[print(word, end=" ") for (word, occurrences) in words_count.items() if occurrences % 2 == 1]
