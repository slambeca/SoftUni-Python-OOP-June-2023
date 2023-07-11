from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("Happy Paws")

    def test_correct_initializing(self):
        self.assertEqual("Happy Paws", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_with_invalid_quantity_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("Royal Canin", 0)

        self.assertEqual("Quantity cannot be equal to or less than 0", str(ve.exception))

    def test_add_food_for_first_time_with_valid_quantity(self):
        result = self.pet_shop.add_food("Royal Canin", 10)

        self.assertEqual("Successfully added 10.00 grams of Royal Canin.", result)

    def test_add_food_for_second_time_with_valid_quantity(self):
        self.pet_shop.add_food("Royal Canin", 10)
        result = self.pet_shop.add_food("Royal Canin", 10)

        self.assertEqual("Successfully added 10.00 grams of Royal Canin.", result)
        self.assertEqual({"Royal Canin": 20}, self.pet_shop.food)

    def test_add_pet_which_is_already_added_raise_exception(self):
        self.pet_shop.add_pet("Sharo")

        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Sharo")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_which_is_not_in_the_list(self):
        result = self.pet_shop.add_pet("Sharo")

        self.assertEqual(["Sharo"], self.pet_shop.pets)
        self.assertEqual("Successfully added Sharo.", result)

    def test_feed_pet_with_invalid_pet_name_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Royal Canin", "Sharo")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_invalid_food_name(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_food("Pedigree", 100)
        result = self.pet_shop.feed_pet("Royal Canin", "Sharo")

        self.assertEqual("You do not have Royal Canin", result)

    def test_feed_but_food_is_less_than_100(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_food("Pedigree", 99)

        result = self.pet_shop.feed_pet("Pedigree", "Sharo")

        self.assertEqual("Adding food...", result)
        self.assertEqual({'Pedigree': 1099.0}, self.pet_shop.food)

    def test_feed_correctly(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_food("Pedigree", 200)

        result = self.pet_shop.feed_pet("Pedigree", "Sharo")

        self.assertEqual("Sharo was successfully fed", result)
        self.assertEqual({"Pedigree": 100}, self.pet_shop.food)

    def test_correct__str__method(self):
        self.pet_shop.add_pet("Sharo")
        self.pet_shop.add_pet("Kostadin")

        result = str(self.pet_shop)
        expected_result = f"Shop Happy Paws:\nPets: Sharo, Kostadin"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()