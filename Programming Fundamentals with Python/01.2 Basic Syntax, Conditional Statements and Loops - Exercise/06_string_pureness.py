number = int(input())

for _ in range(number):
    text = input()
    is_text_pure = True
    for i in range(len(text)):
        if text[i] in [",", ".", "_"]:
            is_text_pure = False

    if is_text_pure:
        print(f"{text} is pure.")
    else:
        print(f"{text} is not pure!")
