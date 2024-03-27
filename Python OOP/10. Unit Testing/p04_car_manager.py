class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")

        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")

        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")

        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")

        self.__fuel_amount += fuel

        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


import unittest


class CarManagerTests(unittest.TestCase):
    def setUp(self):
        self.car = Car("Audi", "RS6", 15, 65)

    def test_car_initialization(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("RS6", self.car.model)
        self.assertEqual(15, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_make_properties(self):
        self.assertEqual("Audi", self.car._Car__make)
        self.car.make = "BMW"

        test_makes = ["", None, 0, False]
        for make in test_makes:
            with self.assertRaises(Exception) as ex:
                self.car.make = make
            self.assertEqual("Make cannot be null or empty!", str(ex.exception))
            self.assertEqual("BMW", self.car._Car__make)

    def test_car_model_properties(self):
        self.assertEqual("RS6", self.car._Car__model)
        self.car.model = "A6"

        test_models = ["", None, 0, False]
        for model in test_models:
            with self.assertRaises(Exception) as ex:
                self.car.model = model
            self.assertEqual("Model cannot be null or empty!", str(ex.exception))
            self.assertEqual("A6", self.car._Car__model)

    def test_car_fuel_consumption_properties(self):
        self.assertEqual(15, self.car._Car__fuel_consumption)
        self.car.fuel_consumption = 12

        test_fuel = [0, -15]
        for fuel in test_fuel:
            with self.assertRaises(Exception) as ex:
                self.car.fuel_consumption = fuel
            self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
            self.assertEqual(12, self.car._Car__fuel_consumption)

    def test_car_fuel_capacity_properties(self):
        self.assertEqual(65, self.car._Car__fuel_capacity)
        self.car.fuel_capacity = 70

        test_fuel_capacities = [0, -20]
        for fuel_capacity in test_fuel_capacities:
            with self.assertRaises(Exception) as ex:
                self.car.fuel_capacity = fuel_capacity
            self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
            self.assertEqual(70, self.car._Car__fuel_capacity)

    def test_car_fuel_amount_properties(self):
        self.assertEqual(0, self.car._Car__fuel_amount)
        self.car.fuel_amount = 15

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -10

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))
        self.assertEqual(15, self.car._Car__fuel_amount)

    def test_car_refuel_method(self):
        self.assertEqual(0, self.car._Car__fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car._Car__fuel_amount)

        self.car.refuel(10)
        self.assertEqual(20, self.car._Car__fuel_amount)

    def test_car_refuel_method_exception(self):
        self.assertEqual(0, self.car._Car__fuel_amount)

        test_refuels = [0, -10]
        for refuel in test_refuels:
            with self.assertRaises(Exception) as ex:
                self.car.refuel(refuel)
            self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
            self.assertEqual(0, self.car._Car__fuel_amount)

    def test_car_refuel_method_overload(self):
        self.assertEqual(0, self.car._Car__fuel_amount)

        self.car.refuel(70)
        self.assertEqual(65, self.car._Car__fuel_amount)

        self.car.refuel(100)
        self.assertEqual(65, self.car._Car__fuel_amount)

    def test_car_drive_method(self):
        self.assertEqual(0, self.car._Car__fuel_amount)
        self.car.refuel(65)
        self.assertEqual(65, self.car._Car__fuel_amount)

        self.car.drive(90)
        self.assertEqual(51.5, self.car._Car__fuel_amount)
        self.car.drive(10)
        self.assertEqual(50, self.car._Car__fuel_amount)

    def test_car_drive_method_exception(self):
        self.assertEqual(0, self.car._Car__fuel_amount)
        self.car.refuel(65)
        self.assertEqual(65, self.car._Car__fuel_amount)

        with self.assertRaises(Exception) as ex:
            self.car.drive(1000000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(65, self.car._Car__fuel_amount)

if __name__ == "__main__":
    unittest.main()