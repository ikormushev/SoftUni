number = int(input())
secret_word = input()

secret_word_list = []
words_list = []

for _ in range(number):
    words = input()

    if secret_word in words:
        secret_word_list.append(words)

    words_list.append(words)

print(words_list)
print(secret_word_list)
