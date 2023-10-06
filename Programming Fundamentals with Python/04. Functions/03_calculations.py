operator = input()
first_number = int(input())
second_number = int(input())


def calculation():
    result = 0

    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number / second_number
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number

    print(f"{result:.0f}")


calculation()
