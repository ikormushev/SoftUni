import unittest
from project.robot import Robot


class RobotTests(unittest.TestCase):
    def setUp(self):
        self.robot = Robot("#1A", "Entertainment", 150, 1000)

    def test_robot_initialization(self):
        self.assertEqual("#1A", self.robot.robot_id)
        self.assertEqual("Entertainment", self.robot._Robot__category)
        self.assertEqual(150, self.robot.available_capacity)
        self.assertEqual(1000, self.robot._Robot__price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], Robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, Robot.PRICE_INCREMENT)

    def test_category_property(self):
        self.assertEqual("Entertainment", self.robot.category)

    def test_category_setter(self):
        self.robot.category = "Military"
        self.assertEqual("Military", self.robot.category)

    def test_category_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Invalid"

        self.assertEqual("Category should be one of '['Military', 'Education', "
                         "'Entertainment', 'Humanoids']'", str(ve.exception))
        self.assertEqual('Entertainment', self.robot.category)

    def test_price_property(self):
        self.assertEqual(1000, self.robot.price)

    def test_price_setter(self):
        self.robot.price = 2000
        self.assertEqual(2000, self.robot.price)

    def test_price_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -200

        self.assertEqual("Price cannot be negative!", str(ve.exception))
        self.assertEqual(1000, self.robot.price)

    def test_upgrade_method_new_components(self):
        component = "Touch-Screen"
        result = self.robot.upgrade(component, 200)

        self.assertEqual('Robot #1A was upgraded with Touch-Screen.', result)
        self.assertEqual(["Touch-Screen"], self.robot.hardware_upgrades)
        self.assertEqual(1300, self.robot.price)

        component = "Touch-ID"
        result = self.robot.upgrade(component, 50)

        self.assertEqual('Robot #1A was upgraded with Touch-ID.', result)
        self.assertEqual(["Touch-Screen", "Touch-ID"], self.robot.hardware_upgrades)
        self.assertEqual(1375, self.robot.price)

    def test_upgrade_method_existing_component(self):
        component = "Touch-Screen"
        self.robot.upgrade(component, 200)
        result = self.robot.upgrade(component, 350)

        self.assertEqual("Robot #1A was not upgraded.", result)
        self.assertEqual(["Touch-Screen"], self.robot.hardware_upgrades)
        self.assertEqual(1300, self.robot.price)

        result = self.robot.upgrade(component, 200)

        self.assertEqual("Robot #1A was not upgraded.", result)
        self.assertEqual(["Touch-Screen"], self.robot.hardware_upgrades)
        self.assertEqual(1300, self.robot.price)

    def test_update_method_new_versions(self):
        result = self.robot.update(1.01, 25)
        self.assertEqual("Robot #1A was updated to version 1.01.", result)
        self.assertEqual([1.01], self.robot.software_updates)
        self.assertEqual(125, self.robot.available_capacity)

        result = self.robot.update(1.02, 5)
        self.assertEqual("Robot #1A was updated to version 1.02.", result)
        self.assertEqual([1.01, 1.02], self.robot.software_updates)
        self.assertEqual(120, self.robot.available_capacity)

    def test_update_method_older_version(self):
        self.robot.update(1.01, 25)
        result = self.robot.update(1.00, 15)

        self.assertEqual("Robot #1A was not updated.", result)
        self.assertEqual([1.01], self.robot.software_updates)
        self.assertEqual(125, self.robot.available_capacity)

    def test_update_method_same_version(self):
        self.robot.update(1.01, 25)
        result = self.robot.update(1.01, 25)

        self.assertEqual("Robot #1A was not updated.", result)
        self.assertEqual([1.01], self.robot.software_updates)
        self.assertEqual(125, self.robot.available_capacity)

    def test_update_method_new_version_no_capacity(self):
        result = self.robot.update(1.01, 160)

        self.assertEqual("Robot #1A was not updated.", result)
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(150, self.robot.available_capacity)

    def test_update_method_new_version_with_existing_versions_no_capacity(self):
        self.robot.update(1.01, 25)
        result = self.robot.update(1.02, 130)

        self.assertEqual("Robot #1A was not updated.", result)
        self.assertEqual([1.01], self.robot.software_updates)
        self.assertEqual(125, self.robot.available_capacity)

    def test_greater_than_method_lower_price(self):
        other_robot = Robot("#1A-a", "Entertainment", 100, 750)
        result = self.robot > other_robot
        self.assertEqual('Robot with ID #1A is more expensive than Robot with ID #1A-a.', result)

    def test_greater_than_method_same_price(self):
        other_robot = Robot("#1B", "Military", 100, 1000)
        result = self.robot > other_robot
        self.assertEqual('Robot with ID #1A costs equal to Robot with ID #1B.', result)

    def test_greater_than_method_higher_price(self):
        other_robot = Robot("#2A", "Entertainment", 100, 2000)
        result = self.robot > other_robot
        self.assertEqual('Robot with ID #1A is cheaper than Robot with ID #2A.', result)


if __name__ == "__main__":
    unittest.main()
