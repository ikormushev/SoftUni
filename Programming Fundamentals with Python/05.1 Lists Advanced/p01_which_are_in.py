first_strings = input().split(", ")
second_strings = input().split(", ")

substrings = []

for i in range(len(first_strings)):
    for y in range(len(second_strings)):
        if first_strings[i] in second_strings[y]:
            substrings.append(first_strings[i])
            break

print(substrings)
