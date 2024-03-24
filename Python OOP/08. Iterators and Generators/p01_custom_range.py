class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.next_element = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.next_element += 1
        if self.next_element <= self.end:
            return self.next_element
        raise StopIteration
