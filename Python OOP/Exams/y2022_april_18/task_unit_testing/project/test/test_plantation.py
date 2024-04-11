import unittest
from project.plantation import Plantation


class PlantationTests(unittest.TestCase):
    def setUp(self):
        self.plantation = Plantation(50)

    def test_plantation_initialization(self):
        self.assertEqual(50, self.plantation._Plantation__size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_property(self):
        self.assertEqual(50, self.plantation.size)

    def test_size_setter(self):
        self.plantation.size = 100
        self.assertEqual(100, self.plantation.size)

    def test_size_setter_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -10

        self.assertEqual("Size must be positive number!", str(ve.exception))
        self.assertEqual(50, self.plantation.size)

    def test_hire_worker_method_new_workers(self):
        result = self.plantation.hire_worker("Sam")
        self.assertEqual("Sam successfully hired.", result)
        self.assertEqual(["Sam"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

        result = self.plantation.hire_worker("Max")
        self.assertEqual("Max successfully hired.", result)
        self.assertEqual(["Sam", "Max"], self.plantation.workers)
        self.assertEqual(2, len(self.plantation.workers))

        result = self.plantation.hire_worker("Alex")
        self.assertEqual("Alex successfully hired.", result)
        self.assertEqual(["Sam", "Max", "Alex"], self.plantation.workers)
        self.assertEqual(3, len(self.plantation.workers))

    def test_hire_worker_method_existing_worker(self):
        self.plantation.hire_worker("Sam")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Sam")

        self.assertEqual("Worker already hired!", str(ve.exception))
        self.assertEqual(["Sam"], self.plantation.workers)
        self.assertEqual(1, len(self.plantation.workers))

    def test_len_method(self):
        self.assertEqual(0, len(self.plantation))

        self.plantation.hire_worker("Sam")
        self.plantation.planting("Sam", "Rose")
        self.assertEqual(1, self.plantation.__len__())

        self.plantation.planting("Sam", "Tulip")
        self.assertEqual(2, self.plantation.__len__())

        self.plantation.hire_worker("Max")
        self.plantation.planting("Max", "Apple Tree")
        self.assertEqual(3, self.plantation.__len__())

    def test_planting_method_not_hired_worker(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Sam", "Rose")

        self.assertEqual("Worker with name Sam is not hired!", str(ve.exception))
        self.assertEqual({}, self.plantation.plants)

    def test_planting_method_hired_worker_first_plantation(self):
        self.plantation.hire_worker("Sam")
        result = self.plantation.planting("Sam", "Rose")

        self.assertEqual("Sam planted it's first Rose.", result)
        self.assertEqual({"Sam": ["Rose"]}, self.plantation.plants)
        self.assertEqual(1, len(self.plantation.plants["Sam"]))

    def test_planting_method_hired_worker_planting_more(self):
        self.plantation.hire_worker("Sam")
        self.plantation.hire_worker("Max")
        result = self.plantation.planting("Sam", "Rose")
        self.assertEqual("Sam planted it's first Rose.", result)
        self.assertEqual({"Sam": ["Rose"]}, self.plantation.plants)
        self.assertEqual(1, len(self.plantation.plants["Sam"]))

        result = self.plantation.planting("Sam", "Tulip")
        self.assertEqual("Sam planted Tulip.", result)
        self.assertEqual({"Sam": ["Rose", "Tulip"]}, self.plantation.plants)
        self.assertEqual(2, len(self.plantation.plants["Sam"]))

        result = self.plantation.planting("Max", "Apple Tree")
        self.assertEqual("Max planted it's first Apple Tree.", result)
        self.assertEqual({"Sam": ["Rose", "Tulip"], "Max": ["Apple Tree"]}, self.plantation.plants)
        self.assertEqual(2, len(self.plantation.plants["Sam"]))
        self.assertEqual(1, len(self.plantation.plants["Max"]))

        result = self.plantation.planting("Max", "Peach Tree")
        self.assertEqual("Max planted Peach Tree.", result)
        self.assertEqual({"Sam": ["Rose", "Tulip"], "Max": ["Apple Tree", "Peach Tree"]}, self.plantation.plants)
        self.assertEqual(2, len(self.plantation.plants["Sam"]))
        self.assertEqual(2, len(self.plantation.plants["Max"]))

    def test_planting_more_than_length_plantations(self):
        self.plantation.size = 2
        self.plantation.hire_worker("Sam")
        self.plantation.hire_worker("Max")
        self.plantation.planting("Sam", "Rose")
        self.plantation.planting("Sam", "Tulip")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Max", "Apple Tree")

        self.assertEqual("The plantation is full!", str(ve.exception))
        self.assertEqual({"Sam": ["Rose", "Tulip"]}, self.plantation.plants)
        self.assertEqual(2, len(self.plantation.plants["Sam"]))

    def test_str_method(self):
        self.assertEqual("Plantation size: 50\n", self.plantation.__str__())
        self.plantation.hire_worker("Sam")
        self.plantation.hire_worker("Max")
        self.plantation.planting("Sam", "Rose")
        self.plantation.planting("Sam", "Tulip")
        self.plantation.planting("Max", "Apple Tree")

        self.assertEqual("Plantation size: 50\nSam, Max\nSam planted: Rose, Tulip\nMax planted: Apple Tree", self.plantation.__str__())

    def test_repr_method(self):
        self.assertEqual("Size: 50\nWorkers: ", self.plantation.__repr__())
        self.plantation.hire_worker("Sam")
        self.plantation.hire_worker("Max")
        self.assertEqual("Size: 50\nWorkers: Sam, Max", self.plantation.__repr__())


if __name__ == "__main__":
    unittest.main()
