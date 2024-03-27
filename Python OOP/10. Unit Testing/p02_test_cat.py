class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def test_cat_initialization(self):
        cat = Cat("Kitty")

        self.assertEqual("Kitty", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_eat_method(self):
        cat = Cat("Kitty")
        cat.eat()

        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)
        self.assertEqual(1, cat.size)

    def test_eat_method_already_eaten(self):
        cat = Cat("Kitty")
        cat.eat()

        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)
        self.assertEqual(1, cat.size)

        with self.assertRaises(Exception) as ex:
            cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)
        self.assertEqual(1, cat.size)

    def test_sleep_method_exception(self):
        cat = Cat("Kitty")
        self.assertFalse(cat.sleepy)
        with self.assertRaises(Exception) as ex:
            cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertFalse(cat.sleepy)

    def test_sleep_method(self):
        cat = Cat("Kitty")
        cat.eat()
        self.assertTrue(cat.sleepy)

        cat.sleep()
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    unittest.main()
