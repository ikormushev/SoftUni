max_points = 0
max_points_word = ""

while True:
    points = 0
    command = input()
    if command == "End of words":
        print(f"The most powerful word is {max_points_word} - {max_points}")
        break
    word = command
    starting_letter = word[0]
    for i in range(len(word)):
        points += ord(word[i])
    if (starting_letter in ["a", "e", "i", "o", "u", "y"]
            or starting_letter in ["A", "E", "I", "O", "U", "Y"]):
        points *= len(word)
    else:
        points = points // len(word)
    if points >= max_points:
        max_points = points
        max_points_word = word

