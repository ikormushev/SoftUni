characters = input().split(", ")

characters_with_values = {x: ord(x) for x in characters}  # dictionary comprehension
print(characters_with_values)
