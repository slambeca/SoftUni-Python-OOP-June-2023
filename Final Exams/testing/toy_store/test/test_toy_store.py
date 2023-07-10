from project.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoreTests(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_correct_initializing(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_add_toy_with_all_valid_input(self):
        result = self.toy_store.add_toy("A", "Lorry")

        self.assertEqual("Lorry", self.toy_store.toy_shelf["A"])
        self.assertEqual("Toy:Lorry placed successfully!", result)

    def test_add_toy_with_invalid_key_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("Z", "Truck")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_which_is_already_added_raise_exception(self):
        self.toy_store.toy_shelf["A"] = "Lorry"

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Lorry")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_on_occupied_shelf_raise_exception(self):
        self.toy_store.toy_shelf["A"] = "Teddy Bear"

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Lorry")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_remove_toy_with_invalid_key_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Z", "Lorry")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_that_is_not_on_the_shelf_raise_exception(self):
        self.toy_store.add_toy("A", "Lorry")

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Truck")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_with_valid_input(self):
        self.toy_store.add_toy("A", "Lorry")
        result = self.toy_store.remove_toy("A", "Lorry")

        self.assertEqual("Remove toy:Lorry successfully!", result)
        self.assertEqual(None, self.toy_store.toy_shelf["A"])


if __name__ == "__main__":
    main()