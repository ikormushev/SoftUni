import unittest
from project.climbing_robot import ClimbingRobot


class ClimbingRobotTests(unittest.TestCase):
    def setUp(self):
        self.climbing_robot = ClimbingRobot("Mountain", "Hands", 20, 500)

    def test_climbing_robot_initialization(self):
        self.assertEqual("Mountain", self.climbing_robot._ClimbingRobot__category)
        self.assertEqual("Hands", self.climbing_robot.part_type)
        self.assertEqual(20, self.climbing_robot.capacity)
        self.assertEqual(500, self.climbing_robot.memory)
        self.assertEqual([], self.climbing_robot.installed_software)
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], ClimbingRobot.ALLOWED_CATEGORIES)

    def test_category_property(self):
        self.assertEqual("Mountain", self.climbing_robot.category)

    def test_category_setter(self):
        self.climbing_robot.category = "Indoor"
        self.assertEqual("Indoor", self.climbing_robot.category)

    def test_category_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.climbing_robot.category = "Outdoor"
        self.assertEqual("Mountain", self.climbing_robot.category)
        self.assertEqual("Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']",
                         str(ve.exception))
        self.assertEqual([], self.climbing_robot.installed_software)

    def test_get_used_capacity_method(self):
        self.assertEqual(0, self.climbing_robot.get_used_capacity())
        GPS = {"name": "GPS", "capacity_consumption": 5, "memory_consumption": 20}
        self.climbing_robot.install_software(GPS)
        self.assertEqual(5, self.climbing_robot.get_used_capacity())

        GPS = {"name": "GPS", "capacity_consumption": 3, "memory_consumption": 30}
        self.climbing_robot.install_software(GPS)
        self.assertEqual(8, self.climbing_robot.get_used_capacity())

    def test_get_available_capacity_method(self):
        self.assertEqual(20, self.climbing_robot.get_available_capacity())
        GPS = {"name": "GPS", "capacity_consumption": 10, "memory_consumption": 20}
        self.climbing_robot.install_software(GPS)
        self.assertEqual(10, self.climbing_robot.get_available_capacity())

        GPS = {"name": "GPS", "capacity_consumption": 5, "memory_consumption": 20}
        self.climbing_robot.install_software(GPS)
        self.assertEqual(5, self.climbing_robot.get_available_capacity())

    def test_get_used_memory_method(self):
        self.assertEqual(0, self.climbing_robot.get_used_memory())
        GPS = {"name": "GPS", "capacity_consumption": 5, "memory_consumption": 100}
        self.climbing_robot.install_software(GPS)
        self.assertEqual(100, self.climbing_robot.get_used_memory())

        GPS = {"name": "GPS", "capacity_consumption": 5, "memory_consumption": 200}
        self.climbing_robot.install_software(GPS)
        self.assertEqual(300, self.climbing_robot.get_used_memory())

    def test_get_available_memory_method(self):
        self.assertEqual(500, self.climbing_robot.get_available_memory())
        GPS = {"name": "GPS", "capacity_consumption": 10, "memory_consumption": 200}
        self.climbing_robot.install_software(GPS)
        self.assertEqual(300, self.climbing_robot.get_available_memory())

        GPS = {"name": "GPS", "capacity_consumption": 10, "memory_consumption": 100}
        self.climbing_robot.install_software(GPS)
        self.assertEqual(200, self.climbing_robot.get_available_memory())

    def test_install_software_method(self):
        GPS = {"name": "GPS", "capacity_consumption": 5, "memory_consumption": 20}
        result = self.climbing_robot.install_software(GPS)
        self.assertEqual([{"name": "GPS", "capacity_consumption": 5, "memory_consumption": 20}],
                         self.climbing_robot.installed_software)
        self.assertEqual("Software 'GPS' successfully installed on Mountain part.", result)

        camera_filters = {"name": "Camera Filters", "capacity_consumption": 3, "memory_consumption": 10}
        result = self.climbing_robot.install_software(camera_filters)
        self.assertEqual([{"name": "GPS", "capacity_consumption": 5, "memory_consumption": 20},
                          {"name": "Camera Filters", "capacity_consumption": 3, "memory_consumption": 10}],
                         self.climbing_robot.installed_software)
        self.assertEqual("Software 'Camera Filters' successfully installed on Mountain part.", result)

    def test_install_software_method_not_enough_capacity(self):
        GPS = {"name": "GPS", "capacity_consumption": 25, "memory_consumption": 20}
        result = self.climbing_robot.install_software(GPS)
        self.assertEqual("Software 'GPS' cannot be installed on Mountain part.", result)
        self.assertEqual([], self.climbing_robot.installed_software)

    def test_install_software_method_not_enough_memory(self):
        GPS = {"name": "GPS", "capacity_consumption": 5, "memory_consumption": 501}
        result = self.climbing_robot.install_software(GPS)
        self.assertEqual("Software 'GPS' cannot be installed on Mountain part.", result)
        self.assertEqual([], self.climbing_robot.installed_software)

    def test_install_software_method_not_enough_memory_and_capacity(self):
        GPS = {"name": "GPS", "capacity_consumption": 21, "memory_consumption": 501}
        result = self.climbing_robot.install_software(GPS)
        self.assertEqual("Software 'GPS' cannot be installed on Mountain part.", result)
        self.assertEqual([], self.climbing_robot.installed_software)


if __name__ == "__main__":
    unittest.main()