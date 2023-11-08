# first_way
import re
strings_number = int(input())

for _ in range(strings_number):
    given_string = input()
    name_pattern = r"\@[a-zA-Z]+\|"
    age_pattern = r"\#\d+\*"
    name = re.search(name_pattern, given_string)[0][1:-1]
    age = re.search(age_pattern, given_string)[0][1:-1]
    print(f"{name} is {age} years old.")

# another_way
# strings_number = int(input())
#
# for _ in range(strings_number):
#     given_string = list(input())
#     at_index = given_string.index("@")
#     bar_index = given_string.index("|")
#     name = "".join(given_string[at_index + 1:bar_index])
#
#     number_sign_index = given_string.index("#")
#     star_index = given_string.index("*")
#     age = "".join(given_string[number_sign_index + 1:star_index])
#     print(f"{name} is {age} years old.")
