import unittest
from project.tennis_player import TennisPlayer


class TennisPlayerTests(unittest.TestCase):
    def setUp(self):
        self.tennis_player = TennisPlayer("Georgi", 19, 100)

    def test_tennis_player_initialization(self):
        self.assertEqual("Georgi", self.tennis_player._TennisPlayer__name)
        self.assertEqual(19, self.tennis_player._TennisPlayer__age)
        self.assertEqual(100, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_property(self):
        self.assertEqual("Georgi", self.tennis_player.name)

    def test_name_setter(self):
        self.tennis_player.name = "Presian"
        self.assertEqual("Presian", self.tennis_player.name)

    def test_name_setter_name_with_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "AA"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))
        self.assertEqual("Georgi", self.tennis_player.name)

    def test_name_setter_name_with_less_than_two_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "A"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))
        self.assertEqual("Georgi", self.tennis_player.name)

    def test_age_property(self):
        self.assertEqual(19, self.tennis_player.age)

    def test_age_setter(self):
        self.tennis_player.age = 20
        self.assertEqual(20, self.tennis_player.age)

    def test_age_setter_age_less_than_18(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))
        self.assertEqual(19, self.tennis_player.age)

    def test_add_new_win_method_new_tournament(self):
        tournament_name = "Sofia Open"
        result = self.tennis_player.add_new_win(tournament_name)
        self.assertEqual(["Sofia Open"], self.tennis_player.wins)
        self.assertIsNone(result)

        tournament_name = "Australia Open"
        result = self.tennis_player.add_new_win(tournament_name)
        self.assertEqual(["Sofia Open", "Australia Open"], self.tennis_player.wins)
        self.assertIsNone(result)

    def test_add_new_win_method_old_tournament(self):
        tournament_name = "Sofia Open"
        result = self.tennis_player.add_new_win(tournament_name)

        result = self.tennis_player.add_new_win(tournament_name)
        self.assertEqual("Sofia Open has been already added to the list of wins!", result)
        self.assertEqual(["Sofia Open"], self.tennis_player.wins)

    def test_less_than_operator_less_points(self):
        opponent = TennisPlayer("Presian", 19, 200)
        result = self.tennis_player < opponent
        self.assertEqual("Presian is a top seeded player and he/she is better than Georgi", result)

    def test_less_than_operator_more_points(self):
        opponent = TennisPlayer("Presian", 19, 50)
        result = self.tennis_player < opponent
        self.assertEqual("Georgi is a better player than Presian", result)

    def test_less_than_operator_equal_points(self):
        opponent = TennisPlayer("Presian", 19, 100)
        result = self.tennis_player < opponent
        self.assertEqual("Georgi is a better player than Presian", result)

    def test_str_method_no_wins(self):
        expected_result = "Tennis Player: Georgi\nAge: 19\nPoints: 100.0\nTournaments won: "
        self.assertEqual(expected_result, str(self.tennis_player))

    def test_str_method_with_wins(self):
        self.tennis_player.add_new_win("Sofia Open")
        self.tennis_player.add_new_win("Australia Open")

        expected_result = "Tennis Player: Georgi\nAge: 19\nPoints: 100.0\nTournaments won: Sofia Open, Australia Open"
        self.assertEqual(expected_result, str(self.tennis_player))

if __name__ == "__main__":
    unittest.main()
