import re


def check_string(given_string: str):
    first_letter = strings[i][0]
    number = int(strings[i][1:-1])
    second_letter = strings[i][-1]
    first_letter_position = alphabet.index(first_letter.lower()) + 1
    second_letter_position = alphabet.index(second_letter.lower()) + 1

    if first_letter.isupper():
        number /= first_letter_position
    elif first_letter.islower():
        number *= first_letter_position

    if second_letter.isupper():
        number -= second_letter_position
    elif second_letter.islower():
        number += second_letter_position

    return number


regex_pattern = r"[a-zA-Z]\d+[a-zA-Z]"
strings = re.findall(regex_pattern, input())
alphabet = [chr(x) for x in range(ord("a"), ord("z") + 1)]
total_sum = 0

for i in range(len(strings)):
    whole_string = strings[i]
    total_sum += check_string(whole_string)

print(f"{total_sum:.2f}")
