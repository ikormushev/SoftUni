class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class IntegerListTests(unittest.TestCase):

    def test_integer_list_initialization(self):
        new_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], new_list._IntegerList__data)

    def test_integer_list_initialization_with_no_integers(self):
        new_list = IntegerList(1.1, "1", True)
        self.assertEqual([], new_list._IntegerList__data)

    def test_get_data_method(self):
        new_list = IntegerList(1, 2, 3)
        self.assertEqual([1, 2, 3], new_list.get_data())

    def test_add_method(self):
        new_list = IntegerList(1, 2, 3)

        result = new_list.add(4)
        self.assertEqual([1, 2, 3, 4], new_list.get_data())
        self.assertEqual(result, new_list.get_data())

        result = new_list.add(5)
        self.assertEqual([1, 2, 3, 4, 5], new_list.get_data())
        self.assertEqual(result, new_list.get_data())

    def test_add_method_exception(self):
        new_list = IntegerList(1, 2, 3)
        test_elements = ["4", 4.4, True, [4]]

        for el in test_elements:
            result = None
            with self.assertRaises(ValueError) as ex:
                result = new_list.add(el)

            self.assertEqual("Element is not Integer", str(ex.exception))
            self.assertIsNone(result)
            self.assertEqual([1, 2, 3], new_list.get_data())

    def test_remove_index_method(self):
        new_list = IntegerList(1, 2, 3)
        result = new_list.remove_index(0)

        self.assertEqual([2, 3], new_list.get_data())
        self.assertEqual(1, result)

    def test_remove_index_method_exception_with_index_equal_to_length(self):
        new_list = IntegerList(1, 2, 3)
        result = None

        with self.assertRaises(IndexError) as ex:
            result = new_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([1, 2, 3], new_list.get_data())
        self.assertIsNone(result)

    def test_remove_index_method_exception_with_index_larger_than_length(self):
        new_list = IntegerList(1, 2, 3)
        result = None

        with self.assertRaises(IndexError) as ex:
            result = new_list.remove_index(4)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([1, 2, 3], new_list.get_data())
        self.assertIsNone(result)

    def test_get_method(self):
        new_list = IntegerList(1, 2, 3)

        result = new_list.get(2)
        self.assertEqual([1, 2, 3], new_list.get_data())
        self.assertEqual(3, result)

    def test_get_method_with_index_equal_to_length(self):
        new_list = IntegerList(1, 2, 3)
        result = None

        with self.assertRaises(IndexError) as ex:
            result = new_list.get(3)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([1, 2, 3], new_list.get_data())
        self.assertIsNone(result)

    def test_get_method_with_index_larger_than_length(self):
        new_list = IntegerList(1, 2, 3)
        result = None

        with self.assertRaises(IndexError) as ex:
            result = new_list.get(4)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([1, 2, 3], new_list.get_data())
        self.assertIsNone(result)

    def test_insert_method(self):
        new_list = IntegerList(1, 2, 3)
        result = new_list.insert(0, 0)

        self.assertEqual([0, 1, 2, 3], new_list.get_data())
        self.assertIsNone(result)

    def test_insert_method_with_invalid_index_and_valid_element(self):
        new_list = IntegerList(1, 2, 3)
        result = None

        with self.assertRaises(IndexError) as ex:
            result = new_list.insert(4, 4)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([1, 2, 3], new_list.get_data())
        self.assertIsNone(result)

    def test_insert_method_with_valid_index_and_invalid_element(self):
        new_list = IntegerList(1, 2, 3)
        test_elements = ["4", 4.4, True, [4]]
        result = None

        for el in test_elements:
            result = None
            with self.assertRaises(ValueError) as ex:
                result = new_list.insert(0, el)

            self.assertEqual("Element is not Integer", str(ex.exception))
            self.assertEqual([1, 2, 3], new_list.get_data())
            self.assertIsNone(result)

    def test_get_biggest_method(self):
        new_list = IntegerList(10, 0, -8)
        result = new_list.get_biggest()

        self.assertEqual(10, result)

    def test_get_biggest_method_with_negatives_only(self):
        new_list = IntegerList(-100, -49, -1)
        result = new_list.get_biggest()

        self.assertEqual(-1, result)

    def test_get_index_method(self):
        new_list = IntegerList(1, 2, 3)
        result = new_list.get_index(1)
        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()