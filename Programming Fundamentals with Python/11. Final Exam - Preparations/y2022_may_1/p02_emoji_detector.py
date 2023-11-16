import re

emoji_pattern = r"((?:\:\:)|(?:\*\*))(?P<emoji>[A-Z][a-z]{2,})\1"

given_string = input()

numbers_in_string = re.findall(r"\d", given_string)
cool_threshold = 1
for number in numbers_in_string:
    cool_threshold *= int(number)

emojis = re.finditer(emoji_pattern, given_string)
total_emojis = 0
cool_emojis = []

for emoji in emojis:
    emoji_info = emoji.groupdict()
    total_emojis += 1
    found_emoji = list(emoji_info["emoji"])
    emoji_coolness = sum([ord(letter) for letter in found_emoji])
    if emoji_coolness > cool_threshold:
        cool_emojis.append(emoji.group())

print(f"Cool threshold: {cool_threshold}")
print(f"{total_emojis} emojis found in the text. The cool ones are:")
[print(x) for x in cool_emojis]
