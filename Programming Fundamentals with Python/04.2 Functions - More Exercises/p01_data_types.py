data_type = input()
input_result = input()


def options_depending_on_data_type(d, r):
    action = 0
    if d == "int":
        action = int(r) * 2
    elif d == "real":
        action = float(r) * 1.5
        action = f"{action:.2f}"
    elif d == "string":
        action = "$" + r + "$"

    return action


print(options_depending_on_data_type(data_type, input_result))
