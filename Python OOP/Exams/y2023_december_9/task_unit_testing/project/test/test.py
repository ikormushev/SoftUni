import unittest
from project.railway_station import RailwayStation
from collections import deque


class RailwayStationTests(unittest.TestCase):
    def setUp(self):
        self.railway_station = RailwayStation("Station")

    def test_railway_station_initialization_valid_name(self):
        self.assertEqual("Station", self.railway_station._RailwayStation__name)
        self.assertEqual(deque(), self.railway_station.arrival_trains)
        self.assertEqual(deque(), self.railway_station.departure_trains)

    def test_name_property(self):
        self.assertEqual("Station", self.railway_station.name)

    def test_name_setter_less_than_three_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = "Na"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))
        self.assertEqual("Station", self.railway_station.name)

    def test_name_setter_less_three_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.railway_station.name = "Nan"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))
        self.assertEqual("Station", self.railway_station.name)

    def test_new_arrival_on_board_method(self):
        info = "Berlin - Sofia, 10 PM"
        self.railway_station.new_arrival_on_board(info)
        self.assertEqual(deque(["Berlin - Sofia, 10 PM"]), self.railway_station.arrival_trains)

        info = "Berlin - London, 11 PM"
        self.railway_station.new_arrival_on_board(info)
        self.assertEqual(deque(["Berlin - Sofia, 10 PM", "Berlin - London, 11 PM"]),
                         self.railway_station.arrival_trains)

    def test_train_has_arrived_method_different_first_arrival(self):
        info = "Berlin - Sofia, 10 PM"
        self.railway_station.new_arrival_on_board(info)

        info = "Berlin - London, 11 PM"
        self.railway_station.new_arrival_on_board(info)

        result = self.railway_station.train_has_arrived(info)
        self.assertEqual("There are other trains to arrive before Berlin - London, 11 PM.", result)
        self.assertEqual(deque(["Berlin - Sofia, 10 PM", "Berlin - London, 11 PM"]),
                         self.railway_station.arrival_trains)
        self.assertEqual(deque(), self.railway_station.departure_trains)

    def test_train_has_arrived_method_same_first_arrival(self):
        info = "Berlin - Sofia, 10 PM"
        self.railway_station.new_arrival_on_board(info)

        info = "Berlin - London, 11 PM"
        self.railway_station.new_arrival_on_board(info)

        result = self.railway_station.train_has_arrived("Berlin - Sofia, 10 PM")
        self.assertEqual("Berlin - Sofia, 10 PM is on the platform and will leave in 5 minutes.", result)
        self.assertEqual(deque(["Berlin - London, 11 PM"]),
                         self.railway_station.arrival_trains)
        self.assertEqual(deque(["Berlin - Sofia, 10 PM"]), self.railway_station.departure_trains)

    def test_train_has_left_method_different_first_departure(self):
        info = "Berlin - Sofia, 10 PM"
        self.railway_station.new_arrival_on_board(info)

        info = "Berlin - London, 11 PM"
        self.railway_station.new_arrival_on_board(info)
        self.railway_station.train_has_arrived("Berlin - Sofia, 10 PM")
        result = self.railway_station.train_has_left(info)

        self.assertFalse(result)
        self.assertEqual(deque(["Berlin - Sofia, 10 PM"]), self.railway_station.departure_trains)

    def test_train_has_left_method_same_first_departure(self):
        info = "Berlin - Sofia, 10 PM"
        self.railway_station.new_arrival_on_board(info)

        info = "Berlin - London, 11 PM"
        self.railway_station.new_arrival_on_board(info)
        self.railway_station.train_has_arrived("Berlin - Sofia, 10 PM")
        result = self.railway_station.train_has_left("Berlin - Sofia, 10 PM")

        self.assertTrue(result)
        self.assertEqual(deque([]), self.railway_station.departure_trains)


if __name__ == "__main__":
    unittest.main()
