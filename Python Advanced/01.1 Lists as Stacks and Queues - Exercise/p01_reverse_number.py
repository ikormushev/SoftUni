input_string = input().split()

while input_string:
    if len(input_string) == 1:
        print(input_string.pop())
    else:
        print(input_string.pop(), end=" ")
