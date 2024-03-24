class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.dict_items = iter(dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.dict_items)
        except StopIteration:
            raise StopIteration

    # def __iter__(self):
    #     return iter(self.dictionary.items())  # possible way, but not for Judge
