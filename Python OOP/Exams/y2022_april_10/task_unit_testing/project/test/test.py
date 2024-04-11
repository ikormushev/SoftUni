import unittest
from project.movie import Movie


class MovieTests(unittest.TestCase):
    def setUp(self):
        self.movie = Movie("Avengers: Endgame", 2019, 8.4)

    def test_movie_initialization(self):
        self.assertEqual("Avengers: Endgame", self.movie._Movie__name)
        self.assertEqual(2019, self.movie._Movie__year)
        self.assertEqual(8.4, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_property(self):
        self.assertEqual("Avengers: Endgame", self.movie.name)

    def test_name_setters(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))
        self.assertEqual("Avengers: Endgame", self.movie.name)

    def test_year_property(self):
        self.assertEqual(2019, self.movie.year)

    def test_year_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        self.assertEqual("Year is not valid!", str(ve.exception))
        self.assertEqual(2019, self.movie.year)

    def test_add_actor_method_new_actors(self):
        self.movie.add_actor("Robert Downey Jr.")
        self.assertEqual(["Robert Downey Jr."], self.movie.actors)

        self.movie.add_actor("Chris Evans")
        self.assertEqual(["Robert Downey Jr.", "Chris Evans"], self.movie.actors)

        self.movie.add_actor("Scarlett Johansson")
        self.assertEqual(["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson"], self.movie.actors)

    def test_add_actor_method_existing_actor(self):
        self.movie.add_actor("Robert Downey Jr.")
        result = self.movie.add_actor("Robert Downey Jr.")
        self.assertEqual("Robert Downey Jr. is already added in the list of actors!", result)
        self.assertEqual(["Robert Downey Jr."], self.movie.actors)

    def test_greater_than_operator_first_movie_higher_rating(self):
        other_movie = Movie("Avengers: Age of Ultron", 2015, 7.3)
        result = self.movie > other_movie

        self.assertEqual('"Avengers: Endgame" is better than "Avengers: Age of Ultron"', result)

    def test_greater_than_operator_second_movie_higher_rating(self):
        other_movie = Movie("The Lord of the Rings: The Return of the King", 2003, 9.0)
        result = self.movie > other_movie

        self.assertEqual(f'"The Lord of the Rings: The Return of the King" '
                         f'is better than "Avengers: Endgame"', result)

    def test_repr_method(self):
        self.movie.add_actor("Robert Downey Jr.")
        self.movie.add_actor("Chris Evans")
        self.movie.add_actor("Scarlett Johansson")

        self.assertEqual(f"Name: Avengers: Endgame\nYear of Release: 2019\n"
                         f"Rating: 8.40\nCast: Robert Downey Jr., Chris Evans, Scarlett Johansson", str(self.movie))


if __name__ == "__main__":
    unittest.main()
