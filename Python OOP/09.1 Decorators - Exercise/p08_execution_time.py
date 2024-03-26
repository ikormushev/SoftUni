from time import time


def exec_time(function):
    def wrapper(*args, **kwargs):

        start_time = time()
        function(*args, **kwargs)
        end_time = time()
        return end_time - start_time

    return wrapper
