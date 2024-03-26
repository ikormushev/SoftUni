import unittest
from project.trip import Trip


class TripTests(unittest.TestCase):
    def setUp(self):
        self.trip = Trip(5000, 5, True)

    def test_trip_initialization(self):
        self.assertEqual(5000, self.trip.budget)
        self.assertEqual(5, self.trip._travelers)
        self.assertTrue(self.trip._is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual({'New Zealand': 7500, 'Australia': 5700,
                          'Brazil': 6200, 'Bulgaria': 500}, Trip.DESTINATION_PRICES_PER_PERSON)

    def test_travelers_property(self):
        self.assertEqual(5, self.trip.travelers)

    def test_travelers_setter(self):
        self.trip.travelers = 10
        self.assertEqual(10, self.trip.travelers)

        self.trip.travelers = 1
        self.assertEqual(1, self.trip.travelers)

    def test_travelers_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual("At least one traveler is required!", str(ve.exception))
        self.assertEqual(5, self.trip.travelers)

    def test_is_family_property(self):
        self.assertTrue(self.trip.is_family)

    def test_is_family_setter(self):
        self.trip.is_family = False
        self.assertFalse(self.trip.is_family)

        self.trip.is_family = True
        self.assertTrue(self.trip.is_family)

    def test_is_family_setter_one_traveler(self):
        new_trip = Trip(5000, 1, False)
        new_trip.is_family = True
        self.assertFalse(new_trip.is_family)

    def test_book_a_trip_method_not_offered_destination(self):
        result = self.trip.book_a_trip("USA")
        self.assertEqual("This destination is not in our offers, please choose a new one!", result)

    def test_a_book_trip_enough_budget_is_family(self):
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual("Successfully booked destination Bulgaria! "
                         "Your budget left is 2750.00", result)
        self.assertEqual({"Bulgaria": 2250}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(2750, self.trip.budget)

    def test_a_book_trip_enough_budget_is_not_a_family(self):
        new_trip = Trip(15000, 2, False)
        result = new_trip.book_a_trip("Australia")

        self.assertEqual("Successfully booked destination Australia! "
                         "Your budget left is 3600.00", result)
        self.assertEqual({"Australia": 11400}, new_trip.booked_destinations_paid_amounts)
        self.assertEqual(3600, new_trip.budget)

    def test_a_book_trip_enough_budget_is_family_not_enough_budget(self):
        result = self.trip.book_a_trip("Brazil")

        self.assertEqual("Your budget is not enough!", result)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(5000, self.trip.budget)

    def test_a_book_trip_enough_budget_is_not_a_family_not_enough_budget(self):
        new_trip = Trip(6000, 2, False)
        result = new_trip.book_a_trip("New Zealand")

        self.assertEqual("Your budget is not enough!", result)
        self.assertEqual({}, new_trip.booked_destinations_paid_amounts)
        self.assertEqual(6000, new_trip.budget)

    def test_booking_status_method_no_bookings(self):
        result = self.trip.booking_status()
        self.assertEqual("No bookings yet. Budget: 5000.00", result)

    def test_booking_status_one_booking(self):
        self.trip.book_a_trip("Bulgaria")
        result = self.trip.booking_status()
        expected_result = """Booked Destination: Bulgaria
Paid Amount: 2250.00\nNumber of Travelers: 5
Budget Left: 2750.00"""

        self.assertEqual(expected_result, result)

    def test_booking_status_more_bookings(self):
        new_trip = Trip(100000, 3, True)
        new_trip.book_a_trip("Australia")
        new_trip.book_a_trip("Bulgaria")
        new_trip.book_a_trip("New Zealand")
        new_trip.book_a_trip("Brazil")

        result = new_trip.booking_status()
        expected_result = """Booked Destination: Australia
Paid Amount: 15390.00\nBooked Destination: Brazil
Paid Amount: 16740.00\nBooked Destination: Bulgaria
Paid Amount: 1350.00\nBooked Destination: New Zealand
Paid Amount: 20250.00\nNumber of Travelers: 3
Budget Left: 46270.00"""

        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
