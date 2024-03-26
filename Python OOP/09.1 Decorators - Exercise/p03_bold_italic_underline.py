def make_bold(function):

    def wrapper(*args):
        text = function(*args)
        result = f"<b>{text}</b>"
        return result

    return wrapper


def make_italic(function):
    def wrapper(*args):
        text = function(*args)
        result = f"<i>{text}</i>"
        return result

    return wrapper


def make_underline(function):
    def wrapper(*args):
        text = function(*args)
        result = f"<u>{text}</u>"
        return result

    return wrapper

