from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTests(TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("Lidl", 100.0)
        self.new_shopping_cart = ShoppingCart("Bulgaria", 50.0)

    def test_correct_initializing_of_shopping_cart_object(self):
        self.assertEqual("Lidl", self.shopping_cart.shop_name)
        self.assertEqual(100.0, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_incorrect_shop_name_getter_with_no_upper_case_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "billa"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_correct_shop_name_getter_with_digit_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.shop_name = "Lidl1"

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_with_invalid_price_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.add_to_cart("Tomatoes", 100)

        self.assertEqual("Product Tomatoes cost too much!", str(ve.exception))

    def test_add_to_cart_with_valid_price(self):
        result = self.shopping_cart.add_to_cart("Tomatoes", 50)

        self.assertEqual("Tomatoes product was successfully added to the cart!", result)
        self.assertEqual({"Tomatoes": 50}, self.shopping_cart.products)

    def test_remove_from_cart_with_invalid_key_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shopping_cart.remove_from_cart("Bananas")

        self.assertEqual("No product with name Bananas in the cart!", str(ve.exception))

    def test_remove_from_cart_with_valid_key(self):
        self.shopping_cart.add_to_cart("Bananas", 10)
        self.shopping_cart.add_to_cart("Tomatoes", 90)

        result = self.shopping_cart.remove_from_cart("Bananas")

        self.assertEqual("Product Bananas was successfully removed from the cart!", result)
        self.assertEqual({"Tomatoes": 90}, self.shopping_cart.products)

    def test__add__method_with_another_shopping_cart_instance(self):
        self.shopping_cart.add_to_cart("Bananas", 20)
        self.new_shopping_cart.add_to_cart("Tomatoes", 20)
        result = self.shopping_cart.__add__(self.new_shopping_cart)

        self.assertEqual("LidlBulgaria", result.shop_name)
        self.assertEqual(150.0, result.budget)
        self.assertEqual({"Bananas": 20, "Tomatoes": 20}, result.products)

    def test_buy_products_with_invalid_input_raise_value_error(self):
        self.shopping_cart.products["Bananas"] = 50
        self.shopping_cart.products["Tomatoes"] = 100

        with self.assertRaises(ValueError) as ve:
            total_sum = sum(self.shopping_cart.products.values())
            self.shopping_cart.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with "
                         f"{total_sum - self.shopping_cart.budget:.2f}lv!", str(ve.exception))

    def test_buy_products_with_valid_input(self):
        self.shopping_cart.products["Bananas"] = 10
        self.shopping_cart.products["Tomatoes"] = 90
        total_sum = sum(self.shopping_cart.products.values())
        result = self.shopping_cart.buy_products()

        self.assertEqual(f"Products were successfully bought! Total cost: {total_sum:.2f}lv.", result)


if __name__ == "__main__":
    main()