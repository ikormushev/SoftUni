points = 0

while True:
    command = input()
    if command == "END":
        break
    elif command.lower() not in ["coding", "dog", "cat", "movie"]:
        continue

    event = command
    if event.isupper():
        points += 2
    else:
        points += 1

if points > 5:
    print("You need extra sleep")
else:
    print(points)
