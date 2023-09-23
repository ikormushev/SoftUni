while True:
    command = input()
    text = ""
    if command == "End":
        break
    elif command == "SoftUni":
        continue

    word = command
    for i in range(len(word)):
        text += word[i] * 2
    print(text)
