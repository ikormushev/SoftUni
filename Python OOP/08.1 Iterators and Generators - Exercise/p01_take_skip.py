class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current = -step
        self.nums_passed = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.nums_passed += 1
        if self.nums_passed <= self.count:
            self.current += self.step
            return self.current
        raise StopIteration
