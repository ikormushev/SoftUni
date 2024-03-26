import unittest
from project.second_hand_car import SecondHandCar


class SecondHandCarTests(unittest.TestCase):
    def setUp(self):
        self.second_hand_car = SecondHandCar("BWM X5", "Luxury SUV", 50000, 75000)

    def test_second_hand_car_initialization(self):
        self.assertEqual("BWM X5", self.second_hand_car.model)
        self.assertEqual("Luxury SUV", self.second_hand_car.car_type)
        self.assertEqual(50000, self.second_hand_car._mileage)
        self.assertEqual(75000, self.second_hand_car._price)
        self.assertEqual([], self.second_hand_car.repairs)

    def test_price_property_property(self):
        self.assertEqual(75000, self.second_hand_car.price)

    def test_price_property_setter(self):
        self.second_hand_car.price = 70000
        self.assertEqual(70000, self.second_hand_car.price)

    def test_price_property_setter_exception_with_value_equal_to_one(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 1
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))
        self.assertEqual(75000, self.second_hand_car.price)

    def test_price_property_setter_exception_with_value_less_than_one(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 0.75

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))
        self.assertEqual(75000, self.second_hand_car.price)

    def test_mileage_property_property(self):
        self.assertEqual(50000, self.second_hand_car.mileage)

    def test_mileage_property_setter(self):
        self.second_hand_car.mileage = 55000
        self.assertEqual(55000, self.second_hand_car.mileage)

    def test_mileage_property_setter_exception_with_value_equal_to_a_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 100
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))
        self.assertEqual(50000, self.second_hand_car.mileage)

    def test_price_property_setter_exception_with_value_less_than_a_hundred(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 50

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))
        self.assertEqual(50000, self.second_hand_car.mileage)

    def test_set_promotional_price_method(self):
        result = self.second_hand_car.set_promotional_price(70000)
        self.assertEqual("The promotional price has been successfully set.", result)
        self.assertEqual(70000, self.second_hand_car.price)

    def test_set_promotional_price_method_exception_new_price_equal_price_to_old(self):
        result = None
        with self.assertRaises(ValueError) as ve:
            result = self.second_hand_car.set_promotional_price(75000)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))
        self.assertIsNone(result)
        self.assertEqual(75000, self.second_hand_car.price)

    def test_set_promotional_price_method_exception_new_price_more_than_old_price(self):
        result = None
        with self.assertRaises(ValueError) as ve:
            result = self.second_hand_car.set_promotional_price(80000)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))
        self.assertIsNone(result)
        self.assertEqual(75000, self.second_hand_car.price)

    def test_need_repair_method(self):
        old_car_price = self.second_hand_car.price
        result = self.second_hand_car.need_repair(4000, "Summer wheels")
        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(old_car_price + 4000, self.second_hand_car.price)
        self.assertEqual(["Summer wheels"], self.second_hand_car.repairs)

        old_car_price = self.second_hand_car.price
        result = self.second_hand_car.need_repair(500, "Oil change")
        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(old_car_price + 500, self.second_hand_car.price)
        self.assertEqual(["Summer wheels", "Oil change"], self.second_hand_car.repairs)

    def test_need_repair_exception_with_repair_price_more_than_half_actual_price(self):
        result = self.second_hand_car.need_repair(80000, "New Engine + New Doors")
        self.assertEqual("Repair is impossible!", result)
        self.assertEqual(75000, self.second_hand_car.price)
        self.assertEqual([], self.second_hand_car.repairs)

    def test_greater_than_method_car_type_mismatch(self):
        new_car = SecondHandCar("BWM Z4", "Luxury Sports Car", 50000, 150000)
        result = self.second_hand_car > new_car
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test_greater_than_method(self):
        new_car = SecondHandCar("BWM X4", "Luxury SUV", 100000, 50000)
        result = self.second_hand_car > new_car
        self.assertTrue(result)

    def test_greater_than_method_equal_prices(self):
        new_car = SecondHandCar("BWM X4", "Luxury SUV", 100000, 75000)
        result = self.second_hand_car > new_car
        self.assertFalse(result)

    def test_str_method(self):
        expected_result = ("""Model BWM X5 | Type Luxury SUV | Milage 50000km
Current price: 75000.00 | Number of Repairs: 0""")
        self.assertEqual(expected_result, str(self.second_hand_car))


if __name__ == "__main__":
    unittest.main()
