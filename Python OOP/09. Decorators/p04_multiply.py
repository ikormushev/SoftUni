def multiply(times):
    def decorator(function):
        # the wrapper accepts args and kwargs
        # for protection for later use

        # if only one argument is always given,
        # we can just use number instead
        def wrapper(*args, **kwargs):
            # unpacking the arguments
            result = function(*args, **kwargs)

            return times * result  # wrapper return
        return wrapper  # decorator return

    return decorator  # multiply return


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))  # 39


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))  # 80


@multiply(10)
def add_numbers(n1, n2):
    return n1 + n2


print(add_numbers(5, 4))  # 90
