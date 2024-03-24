class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start_index = 0
        self.current_index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index -= 1
        if self.current_index >= self.start_index:
            return self.iterable[self.current_index]
        raise StopIteration
