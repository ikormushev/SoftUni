import unittest
from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Doggy", "Dog", "Woof-woof")

    def test_mammal_initialization(self):
        self.assertEqual("Doggy", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("Woof-woof", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method(self):
        self.assertEqual("Doggy makes Woof-woof", self.mammal.make_sound())

    def test_get_kingdom_method(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_method(self):
        self.assertEqual("Doggy is of type Dog", self.mammal.info())


if __name__ == "__main__":
    unittest.main()