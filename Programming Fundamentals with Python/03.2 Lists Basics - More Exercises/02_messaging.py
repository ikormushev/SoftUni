numbers = input().split(" ")
text_string = list(input())

numbers_integers = []
hidden_message = ""

for i in range(len(numbers)):
    numbers_integers.append(int(numbers[i]))

for y in range(len(numbers_integers)):
    index = 0
    for j in range(len(str(numbers_integers[y]))):
        index += int(str(numbers_integers[y])[j])

    if index >= len(text_string):
        while index >= len(text_string):
            index -= len(text_string)

    hidden_message += text_string[index]
    text_string.pop(index)

print(hidden_message)
