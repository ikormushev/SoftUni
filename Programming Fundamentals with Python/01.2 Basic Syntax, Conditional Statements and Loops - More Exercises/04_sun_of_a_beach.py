text = input()

texts_list = ["sand", "water", "fish", "sun"]
found_word_list = []
appearances = 0


for i in range(len(text)):
    found_word_list += text[i].lower()
    for y in range(len(texts_list)):
        if texts_list[y] in "".join(found_word_list):
            appearances += 1
            found_word_list = []
            break

print(appearances)
