messages_num = int(input())

for _ in range(messages_num):
    number = int(input())
    message = ""
    if number == 86:
        message = "How are you?"
    elif number == 88:
        message = "Hello"
    elif number < 88:
        message = "GREAT!"
    elif number > 88:
        message = "Bye."
    print(message)
