text = input()

points = 0
vowels = ["a", "e", "i", "o", "u"]

points_dict = {
    "a": 1,
    "e": 2,
    "i": 3,
    "o": 4,
    "u": 5,
}

for i in range(0, len(text)):
    if text[i] in vowels:
        points += points_dict[text[i]]

print(points)
