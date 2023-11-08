characters = input()

replaced_characters = ""

for i in range(len(characters)):
    if i == 0:
        replaced_characters += characters[i]
    else:
        if characters[i] != characters[i - 1]:
            replaced_characters += characters[i]

print(replaced_characters)
