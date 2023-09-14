first_word = input()
second_word = input()

first_word_list = list(first_word)

for i in range(len(first_word_list)):
    if first_word_list[i] != second_word[i]:
        first_word_list[i] = second_word[i]
        print("".join(first_word_list))
