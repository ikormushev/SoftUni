def even_odd(*args):
    command = args[-1]
    return [x for x in args[:-1] if x % 2 == 0] if command == "even" else [x for x in args[:-1] if x % 2 == 1]

