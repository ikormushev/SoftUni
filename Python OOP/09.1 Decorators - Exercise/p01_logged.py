def logged(function):
    def wrapper(*args, **kwargs):
        result = f"you called {function.__name__}{args}\n"
        result += f"it returned {function(*args, **kwargs)}"
        return result

    return wrapper
