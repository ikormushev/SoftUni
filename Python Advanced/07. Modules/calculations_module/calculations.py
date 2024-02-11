def basic_calculations(received_string):
    basic_operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "^": lambda x, y: x ** y,
    }

    received_string = received_string.split()
    first_number = float(received_string[0])
    operator = received_string[1]
    second_number = float(received_string[2])

    if operator == "/" and second_number == 0:
        return "Division by 0 not possible!"

    return basic_operations[operator](first_number, second_number)
