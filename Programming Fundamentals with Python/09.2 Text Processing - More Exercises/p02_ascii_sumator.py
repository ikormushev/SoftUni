first_char = input()
second_char = input()
random_string = input()

found_characters = [ord(x) for x in random_string if ord(x) in range(ord(first_char) + 1, ord(second_char))]
characters_sum = sum(found_characters)
print(characters_sum)
