number = float(input())

number_text = ""

if number == 0:
    number_text = "zero"
else:
    if abs(number) < 1 and abs(number) != 0:
        number_text += "small "
    elif abs(number) > 1000000:
        number_text += "large "

    if number > 0:
        number_text += "positive"
    elif number < 0:
        number_text += "negative"

print(number_text)
