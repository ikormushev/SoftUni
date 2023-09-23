key = int(input())
lines_num = int(input())

word_list = []
for i in range(1, lines_num + 1):
    letter = input()
    word_list.append(chr(ord(letter) + key))

print("".join(word_list))
