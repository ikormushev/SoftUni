class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.current = count + 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current >= self.end:
            return self.current
        raise StopIteration
