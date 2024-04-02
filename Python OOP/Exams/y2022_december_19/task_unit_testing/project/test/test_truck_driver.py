import unittest
from project.truck_driver import TruckDriver


class TruckDriverTests(unittest.TestCase):
    def setUp(self):
        self.truck_diver = TruckDriver("Sam", 2.50)

    def test_truck_driver_initialization(self):
        self.assertEqual("Sam", self.truck_diver.name)
        self.assertEqual(2.50, self.truck_diver.money_per_mile)
        self.assertEqual({}, self.truck_diver.available_cargos)
        self.assertEqual(0, self.truck_diver._TruckDriver__earned_money)
        self.assertEqual(0, self.truck_diver.miles)

    def test_truck_driver_earned_money_property(self):
        self.assertEqual(0, self.truck_diver.earned_money)

    def test_truck_driver_earned_money_setter(self):
        self.truck_diver.earned_money = 500
        self.assertEqual(500, self.truck_diver.earned_money)

    def test_truck_driver_earned_money_setter_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_diver.earned_money = -500

        self.assertEqual("Sam went bankrupt.", str(ve.exception))
        self.assertEqual(0, self.truck_diver.earned_money)

    def test_add_cargo_offer_method_new_location(self):
        result = self.truck_diver.add_cargo_offer("Sofia", 300)
        self.assertEqual("Cargo for 300 to Sofia was added as an offer.", result)
        self.assertEqual({"Sofia": 300}, self.truck_diver.available_cargos)

        result = self.truck_diver.add_cargo_offer("Plovdiv", 150)
        self.assertEqual("Cargo for 150 to Plovdiv was added as an offer.", result)
        self.assertEqual({"Sofia": 300, "Plovdiv": 150}, self.truck_diver.available_cargos)

    def test_add_cargo_offer_method_existing_location(self):
        self.truck_diver.add_cargo_offer("Sofia", 300)

        with self.assertRaises(Exception) as ex:
            self.truck_diver.add_cargo_offer("Sofia", 250)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))
        self.assertEqual({"Sofia": 300}, self.truck_diver.available_cargos)

    def test_drive_best_cargo_offer_method_no_offers(self):
        result = self.truck_diver.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)
        self.assertEqual(0, self.truck_diver.earned_money)
        self.assertEqual(0, self.truck_diver.miles)

    def test_eat_method(self):
        self.truck_diver.earned_money = 1000
        self.truck_diver.eat(250)
        self.assertEqual(980, self.truck_diver.earned_money)

        self.truck_diver.eat(100)
        self.assertEqual(980, self.truck_diver.earned_money)

    def test_sleep_method(self):
        self.truck_diver.earned_money = 1000
        self.truck_diver.sleep(1000)
        self.assertEqual(955, self.truck_diver.earned_money)

        self.truck_diver.sleep(900)
        self.assertEqual(955, self.truck_diver.earned_money)

    def test_pump_gas_method(self):
        self.truck_diver.earned_money = 1000
        self.truck_diver.pump_gas(1500)
        self.assertEqual(500, self.truck_diver.earned_money)

        self.truck_diver.pump_gas(150)
        self.assertEqual(500, self.truck_diver.earned_money)

    def test_repair_truck_method(self):
        self.truck_diver.earned_money = 10000
        self.truck_diver.repair_truck(10000)
        self.assertEqual(2500, self.truck_diver.earned_money)

        self.truck_diver.repair_truck(1000)
        self.assertEqual(2500, self.truck_diver.earned_money)

    def test_check_for_activities_method(self):
        self.truck_diver.earned_money = 15000
        self.truck_diver.check_for_activities(10000)
        # every 250 miles -> eat -> 40 times * 20 -> 15000 - 800 = 14200
        # every 1000 miles -> sleep -> 10 times * 45 -> 14200 - 450 = 13750
        # every 1500 miles -> pump_gas -> 6 times * 500 -> 13750 - 3000 = 10750
        # every 10000 miles -> repair_truck -> 1 time * 7500 -> 10750 - 7500 = 3250

        self.assertEqual(3250, self.truck_diver.earned_money)

    def test_drive_best_cargo_offer_method_one_offer(self):
        self.truck_diver.add_cargo_offer("Sofia", 300)
        result = self.truck_diver.drive_best_cargo_offer()

        self.assertEqual(f"Sam is driving 300 to Sofia.", result)
        self.assertEqual(730, self.truck_diver.earned_money)
        self.assertEqual(300, self.truck_diver.miles)

    def test_drive_best_cargo_offer_method_more_than_one_offer(self):
        self.truck_diver.add_cargo_offer("Sofia", 300)
        self.truck_diver.add_cargo_offer("Varna", 600)
        self.truck_diver.add_cargo_offer("Istanbul", 1500)

        result = self.truck_diver.drive_best_cargo_offer()

        self.assertEqual(f"Sam is driving 1500 to Istanbul.", result)
        self.assertEqual(3085, self.truck_diver.earned_money)
        self.assertEqual(1500, self.truck_diver.miles)

    def test_repr_method(self):
        result = self.truck_diver.__repr__()
        self.assertEqual("Sam has 0 miles behind his back.", result)


if __name__ == "__main__":
    unittest.main()
