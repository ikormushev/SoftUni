def even_parameters(function):

    def wrapper(*args):
        for number in args:
            if isinstance(number, int):
                if number % 2 == 0:
                    continue

            return "Please use only even numbers!"
        return function(*args)

    return wrapper
