class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self < other or self == other
