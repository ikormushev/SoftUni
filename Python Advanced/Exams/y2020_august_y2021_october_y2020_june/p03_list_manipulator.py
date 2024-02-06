def list_manipulator(numbers, *args):
    for i in range(len(args)):
        parameter = args[i]
        if parameter == "add":
            next_parameter = args[i + 1]
            new_numbers = list(args[i + 2:])
            if next_parameter == "beginning":
                new_numbers += numbers
                return new_numbers
            elif next_parameter == "end":
                numbers += new_numbers
                return numbers

        elif parameter == "remove":
            next_parameter = args[i + 1]
            if next_parameter == "beginning":
                if i + 2 < len(args):
                    number = args[i + 2]
                    for _ in range(number):
                        numbers.pop(0)
                else:
                    numbers.pop(0)
                return numbers
            elif next_parameter == "end":
                if i + 2 < len(args):
                    number = args[i + 2]
                    for _ in range(number):
                        numbers.pop()
                else:
                    numbers.pop()
                return numbers


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
