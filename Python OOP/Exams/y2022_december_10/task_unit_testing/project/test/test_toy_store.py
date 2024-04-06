import unittest
from project.toy_store import ToyStore


class ToyStoreTests(unittest.TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_toy_store_initialization(self):
        self.assertEqual({"A": None, "B": None, "C": None, "D": None,
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

    def test_add_toy_method_existing_shelves(self):
        result = self.toy_store.add_toy("A", "Car")
        self.assertEqual("Toy:Car placed successfully!", result)
        self.assertEqual({"A": "Car", "B": None, "C": None, "D": None,
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

        result = self.toy_store.add_toy("D", "Lego House")
        self.assertEqual("Toy:Lego House placed successfully!", result)
        self.assertEqual({"A": "Car", "B": None, "C": None, "D": "Lego House",
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

        result = self.toy_store.add_toy("B", "Plane")
        self.assertEqual("Toy:Plane placed successfully!", result)
        self.assertEqual({"A": "Car", "B": "Plane", "C": None, "D": "Lego House",
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

    def test_add_toy_method_unknown_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("Z", "Car")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({"A": None, "B": None, "C": None, "D": None,
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

    def test_add_toy_method_toy_already_on_shelf(self):
        self.toy_store.add_toy("A", "Car")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Car")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))
        self.assertEqual({"A": "Car", "B": None, "C": None, "D": None,
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

    def test_add_toy_method_shelf_taken_with_another_toy(self):
        self.toy_store.add_toy("A", "Car")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Plane")

        self.assertEqual("Shelf is already taken!", str(ex.exception))
        self.assertEqual({"A": "Car", "B": None, "C": None, "D": None,
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

    def test_remove_toy_method_existing_toys_on_shelf(self):
        self.toy_store.add_toy("A", "Car")
        self.toy_store.add_toy("B", "Lego House")
        self.toy_store.add_toy("F", "Plane")

        result = self.toy_store.remove_toy("A", "Car")
        self.assertEqual("Remove toy:Car successfully!", result)
        self.assertEqual({"A": None, "B": "Lego House", "C": None, "D": None,
                          "E": None, "F": "Plane", "G": None}, self.toy_store.toy_shelf)

        result = self.toy_store.remove_toy("B", "Lego House")
        self.assertEqual("Remove toy:Lego House successfully!", result)
        self.assertEqual({"A": None, "B": None, "C": None, "D": None,
                          "E": None, "F": "Plane", "G": None}, self.toy_store.toy_shelf)

        result = self.toy_store.remove_toy("F", "Plane")
        self.assertEqual("Remove toy:Plane successfully!", result)
        self.assertEqual({"A": None, "B": None, "C": None, "D": None,
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

    def test_remove_toy_method_unknown_shelf(self):
        self.toy_store.add_toy("A", "Car")
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Z", "Car")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual({"A": "Car", "B": None, "C": None, "D": None,
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

    def test_remove_toy_method_unknown_toy(self):
        self.toy_store.add_toy("A", "Car")
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Plane")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))
        self.assertEqual({"A": "Car", "B": None, "C": None, "D": None,
                          "E": None, "F": None, "G": None}, self.toy_store.toy_shelf)

if __name__ == "__main__":
    unittest.main()