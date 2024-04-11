import unittest
from project.shopping_cart import ShoppingCart


class ShoppingCartTests(unittest.TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("Lidl", 250)

    def test_shopping_cart_initialization(self):
        self.assertEqual("Lidl", self.shopping_cart._ShoppingCart__shop_name)
        self.assertEqual(250, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_shop_name_property(self):
        self.assertEqual("Lidl", self.shopping_cart.shop_name)

    def test_shop_name_setter(self):
        self.shopping_cart.shop_name = "Kaufland"
        self.assertEqual("Kaufland", self.shopping_cart.shop_name)

    def test_shop_name_setter_name_no_capital_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "kaufland"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))
        self.assertEqual("Lidl", self.shopping_cart.shop_name)

    def test_shop_name_setter_name_with_some_numbers(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "Kau12fland"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))
        self.assertEqual("Lidl", self.shopping_cart.shop_name)

    def test_shop_name_setter_name_with_other_symbols(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "K@ufland"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))
        self.assertEqual("Lidl", self.shopping_cart.shop_name)

    def test_add_to_cart_method_less_than_a_hundred_price(self):
        result = self.shopping_cart.add_to_cart("Apples", 15.50)
        self.assertEqual(f"Apples product was successfully added to the cart!", result)
        self.assertEqual({"Apples": 15.50}, self.shopping_cart.products)

        result = self.shopping_cart.add_to_cart("Bananas", 20.75)
        self.assertEqual("Bananas product was successfully added to the cart!", result)
        self.assertEqual({"Apples": 15.50, "Bananas": 20.75}, self.shopping_cart.products)

    def test_add_to_cart_method_equal_to_a_hundred_price(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("Telephone", 100)

        self.assertEqual("Product Telephone cost too much!", str(ve.exception))
        self.assertEqual({}, self.shopping_cart.products)

    def test_add_to_cart_method_more_than_a_hundred_price(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("SmartTV", 250)

        self.assertEqual("Product SmartTV cost too much!", str(ve.exception))
        self.assertEqual({}, self.shopping_cart.products)

    def test_remove_from_cart_product_existing_product(self):
        self.shopping_cart.add_to_cart("Apples", 15.50)
        self.shopping_cart.add_to_cart("Bananas", 20.75)

        result = self.shopping_cart.remove_from_cart("Apples")
        self.assertEqual("Product Apples was successfully removed from the cart!", result)
        self.assertEqual({"Bananas": 20.75}, self.shopping_cart.products)

        result = self.shopping_cart.remove_from_cart("Bananas")
        self.assertEqual("Product Bananas was successfully removed from the cart!", result)
        self.assertEqual({}, self.shopping_cart.products)

    def test_remove_from_cart_unknown_product(self):
        self.shopping_cart.add_to_cart("Apples", 15.50)
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("Bananas")

        self.assertEqual("No product with name Bananas in the cart!", str(ve.exception))
        self.assertEqual({"Apples": 15.50}, self.shopping_cart.products)

    def test_add_operator(self):
        self.shopping_cart.add_to_cart("Apples", 15.50)
        self.shopping_cart.add_to_cart("Bananas", 20.75)

        other_shopping_cart = ShoppingCart("Kaufland", 200)
        other_shopping_cart.add_to_cart("Tomatoes", 12.36)
        other_shopping_cart.add_to_cart("Potatoes", 10.79)
        other_shopping_cart.add_to_cart("Apples", 10)

        new_shopping_cart = self.shopping_cart + other_shopping_cart

        self.assertEqual("LidlKaufland", new_shopping_cart.shop_name)
        self.assertEqual(450, new_shopping_cart.budget)
        self.assertEqual({"Apples": 10, "Bananas": 20.75, "Tomatoes": 12.36, "Potatoes": 10.79}, new_shopping_cart.products)

    def test_buy_products_enough_budget(self):
        self.shopping_cart.add_to_cart("Apples", 15.50)
        self.shopping_cart.add_to_cart("Bananas", 20.75)
        result = self.shopping_cart.buy_products()

        self.assertEqual("Products were successfully bought! Total cost: 36.25lv.", result)

    def test_buy_products_not_enough_budget(self):
        self.shopping_cart.add_to_cart("TV", 99)
        self.shopping_cart.add_to_cart("Phone", 99)
        self.shopping_cart.add_to_cart("RobotCleaner", 99)

        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with 47.00lv!", str(ve.exception))


if __name__ == "__main__":
    unittest.main()
