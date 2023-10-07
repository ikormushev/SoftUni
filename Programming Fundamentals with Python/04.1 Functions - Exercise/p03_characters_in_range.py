first_character = input()
second_character = input()


def characters_in_range(x, y):
    for i in range(ord(x) + 1, ord(y)):
        print(chr(i), end=" ")


characters_in_range(first_character, second_character)
