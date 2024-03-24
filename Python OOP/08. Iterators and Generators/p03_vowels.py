class vowels:
    VOWELS = ["a", "e", "i", "o", "u", "y"]

    def __init__(self, text: str):
        self.text = text
        self.current_index = -1
        self.text_only_with_vowels = [x for x in self.text if x.lower() in self.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index < len(self.text_only_with_vowels):
            return self.text_only_with_vowels[self.current_index]
        raise StopIteration
