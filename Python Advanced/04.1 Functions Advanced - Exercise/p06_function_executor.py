def func_executor(*args):
    string_to_print = ""
    for function, arguments in args:
        function_result = function(*arguments)
        string_to_print += f"{function.__name__} - {function_result}\n"
    return string_to_print
