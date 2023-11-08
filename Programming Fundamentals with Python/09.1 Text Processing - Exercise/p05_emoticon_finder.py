text = list(input())

for i in range(len(text)):
    if i + 1 < len(text):
        if text[i] == ":":
            print(f"{text[i]}{text[i+1]}")
