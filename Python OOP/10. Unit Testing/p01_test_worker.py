class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Worker", 500, 100)

    def test_worker_initialization(self):
        self.assertEqual("Worker", self.worker.name)
        self.assertEqual(500, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_method_with_enough_energy(self):
        self.test_worker_initialization()

        self.worker.work()
        self.assertEqual(99, self.worker.energy)
        self.assertEqual(500, self.worker.money)

        self.worker.work()
        self.assertEqual(98, self.worker.energy)
        self.assertEqual(1000, self.worker.money)

    def test_work_method_with_energy_less_than_zero(self):
        worker = Worker("Worker", 500, -1)
        self.assertEqual(-1, worker.energy)
        self.assertEqual(0, worker.money)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))
        self.assertEqual(-1, worker.energy)
        self.assertEqual(0, worker.money)

    def test_work_method_with_zero_energy(self):
        worker = Worker("Worker", 500, 0)
        self.assertEqual(0, worker.energy)
        self.assertEqual(0, worker.money)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))
        self.assertEqual(0, worker.energy)
        self.assertEqual(0, worker.money)

    def test_rest_method(self):
        self.worker.rest()

        self.assertEqual(101, self.worker.energy)

    def test_get_info_method(self):
        expected_result = "Worker has saved 0 money."
        self.assertEqual(expected_result, self.worker.get_info())

        self.worker.work()
        expected_result = "Worker has saved 500 money."
        self.assertEqual(expected_result, self.worker.get_info())


if __name__ == "__main__":
    unittest.main()
