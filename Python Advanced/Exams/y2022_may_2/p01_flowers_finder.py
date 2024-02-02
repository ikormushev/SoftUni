from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers = {
    "rose": [False for _ in "rose"],
    "tulip": [False for _ in "tulip"],
    "lotus": [False for _ in "lotus"],
    "daffodil": [False for _ in "daffodil"]
}

is_word_found = False
word_found = ""

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for (flower, occurrences) in flowers.items():
        for i in range(len(flower)):
            if vowel == flower[i] or consonant == flower[i]:
                occurrences[i] = True

        if all(occurrences):
            is_word_found = True
            word_found = flower
            break

    if is_word_found:
        break

if word_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
