def type_check(_type):
    def decorator(function):
        def wrapper(*args):
            for el in args:
                if isinstance(el, _type):
                    continue

                return f"Bad Type"

            return function(*args)
        return wrapper

    return decorator
