import unittest
from project.bookstore import Bookstore


class BookstoreTests(unittest.TestCase):
    def setUp(self):
        self.bookstore = Bookstore(50)

    def test_bookstore_initialization(self):
        self.assertEqual(50, self.bookstore._Bookstore__books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_total_sold_books_property(self):
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_property(self):
        self.assertEqual(50, self.bookstore.books_limit)

    def test_books_limit_setter(self):
        self.bookstore.books_limit = 100
        self.assertEqual(100, self.bookstore.books_limit)

    def test_books_limit_setter_zero_books(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))
        self.assertEqual(50, self.bookstore.books_limit)

    def test_books_limit_setter_negative_books(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -89
        self.assertEqual("Books limit of -89 is not valid", str(ve.exception))
        self.assertEqual(50, self.bookstore.books_limit)

    def test_len_method(self):
        result = len(self.bookstore)
        self.assertEqual(0, result)

    def test_receive_book_method(self):
        result = self.bookstore.receive_book("Mathematics 101", 10)
        self.assertEqual("10 copies of Mathematics 101 are available in the bookstore.", result)
        self.assertEqual({"Mathematics 101": 10}, self.bookstore.availability_in_store_by_book_titles)

        result = self.bookstore.receive_book("Mathematics 101", 5)
        self.assertEqual("15 copies of Mathematics 101 are available in the bookstore.", result)
        self.assertEqual({"Mathematics 101": 15}, self.bookstore.availability_in_store_by_book_titles)

        result = self.bookstore.receive_book("Python Basics", 8)
        self.assertEqual("8 copies of Python Basics are available in the bookstore.", result)
        self.assertEqual({"Mathematics 101": 15, "Python Basics": 8},
                         self.bookstore.availability_in_store_by_book_titles)

    def test_receive_book_method_too_much_books(self):
        self.bookstore.receive_book("Mathematics 101", 10)

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Not enough of this book", 50)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))
        self.assertEqual({"Mathematics 101": 10}, self.bookstore.availability_in_store_by_book_titles)

    def test_sell_book_method_unknown_book(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Mathematics 101", 200)

        self.assertEqual("Book Mathematics 101 doesn't exist!", str(ex.exception))
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_sell_book_method_too_much_of_a_book(self):
        result = self.bookstore.receive_book("Mathematics 101", 10)
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Mathematics 101", 200)

        self.assertEqual("Mathematics 101 has not enough copies to sell. Left: 10", str(ex.exception))
        self.assertEqual({"Mathematics 101": 10}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_sell_book_method(self):
        self.bookstore.receive_book("Mathematics 101", 10)
        self.bookstore.receive_book("Mathematics 101", 5)
        self.bookstore.receive_book("Python Basics", 8)

        result = self.bookstore.sell_book("Mathematics 101", 3)
        self.assertEqual(3, self.bookstore.total_sold_books)
        self.assertEqual("Sold 3 copies of Mathematics 101", result)
        self.assertEqual({"Mathematics 101": 12, "Python Basics": 8},
                         self.bookstore.availability_in_store_by_book_titles)

        result = self.bookstore.sell_book("Python Basics", 8)
        self.assertEqual(11, self.bookstore.total_sold_books)
        self.assertEqual("Sold 8 copies of Python Basics", result)
        self.assertEqual({"Mathematics 101": 12, "Python Basics": 0},
                         self.bookstore.availability_in_store_by_book_titles)

    def test_str_method(self):
        self.bookstore.receive_book("Mathematics 101", 10)
        self.bookstore.receive_book("Mathematics 101", 5)
        self.bookstore.receive_book("Python Basics", 8)

        self.bookstore.sell_book("Mathematics 101", 3)
        self.bookstore.sell_book("Python Basics", 8)
        self.bookstore.sell_book("Mathematics 101", 2)

        self.assertEqual("Total sold books: 13\n"
                         "Current availability: 10\n"
                         " - Mathematics 101: 10 copies\n"
                         " - Python Basics: 0 copies", str(self.bookstore))


if __name__ == "__main__":
    unittest.main()
