import unittest
from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 175.5)

    def test_vehicle_initialization(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method(self):
        self.vehicle.drive(20)
        self.assertEqual(75, self.vehicle.fuel)

        self.vehicle.drive(30)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_drive_method_with_more_fuel_needed_than_fuel_in_vehicle(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(81)

        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(100, self.vehicle.fuel)

    def test_refuel_method_less_than_capacity(self):
        self.vehicle.drive(70)

        self.vehicle.refuel(70)
        self.assertEqual(82.5, self.vehicle.fuel)

        self.vehicle.refuel(10)
        self.assertEqual(92.5, self.vehicle.fuel)

    def test_refuel_method_refuel_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)

        self.assertEqual("Too much fuel", str(ex.exception))
        self.assertEqual(100, self.vehicle.fuel)

    def test_str_method(self):
        result = f"The vehicle has 175.5 horse power with 100 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, str(self.vehicle))


if __name__ == "__main__":
    unittest.main()
