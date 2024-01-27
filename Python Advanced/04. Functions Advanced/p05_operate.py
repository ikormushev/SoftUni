def operate(operator, *args):
    result = args[0]
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    for i in range(1, len(args)):
        next_element = args[i]
        if operator == "/" and next_element == 0:
            continue
        result = operations[operator](result, next_element)

    return result

# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
