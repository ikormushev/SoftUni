given_string = list(input())

for _ in range(given_string.count(" ")):  # by condition, we have to escape whitespace
    given_string.remove(" ")

characters_count = {}

for i in range(len(given_string)):
    given_character = given_string[i]
    if given_character not in characters_count:
        characters_count[given_character] = 1
    else:
        characters_count[given_character] += 1

[print(f"{character} -> {count}") for (character, count) in characters_count.items()]
