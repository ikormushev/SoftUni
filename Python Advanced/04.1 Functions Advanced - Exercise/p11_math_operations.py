def math_operations(*args, **kwargs):

    operations_count = 0
    operations = {
        1: ["a", lambda x: kwargs["a"] + x],
        2: ["s", lambda x: kwargs["s"] - x],
        3: ["d", lambda x: kwargs["d"] / x],
        4: ["m", lambda x: kwargs["m"] * x],
    }
    for i in range(len(args)):
        number = args[i]
        if operations_count >= 4:
            operations_count = 0
        operations_count += 1
        if operations_count == 3 and number == 0:
            continue
        operation_letter = operations[operations_count][0]
        kwargs[operation_letter] = operations[operations_count][1](number)

    sorted_numbers = dict(sorted(kwargs.items(), key=lambda d: (-d[1], d[0])))
    string_to_print = ""

    for (letter, value) in sorted_numbers.items():
        string_to_print += f"{letter}: {value:.1f}\n"

    return string_to_print
