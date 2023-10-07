numbers = input().split(", ")


def reversing_number(y):
    reversed_number = reversed(y)
    return "".join(reversed_number)


def is_number_palindrome(x):
    if x == reversing_number(x):
        return True
    else:
        return False


for i in range(len(numbers)):
    print(is_number_palindrome(numbers[i]))
