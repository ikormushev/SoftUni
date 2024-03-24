def read_next(*args):
    index = 0
    while index < len(args):
        for el in args[index]:
            yield el
        index += 1
