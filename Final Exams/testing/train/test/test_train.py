from unittest import TestCase, main
from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self):
        self.train = Train("Lokomotiv", 100)

    def test_class_attributes(self):
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_correct_initializing(self):
        self.assertEqual("Lokomotiv", self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_but_passenger_is_already_on_the_train_raise_value_error(self):
        self.train.add("Borislav")

        with self.assertRaises(ValueError) as ve:
            self.train.add("Borislav")

        self.assertEqual(Train.PASSENGER_EXISTS.format("Borislav"), str(ve.exception))

    def test_add_passenger_which_is_not_on_the_train_but_there_is_no_capacity_raise_value_error(self):
        self.train.capacity = 1
        self.train.add("Borislav")

        with self.assertRaises(ValueError) as ve:
            self.train.add("Neno")

        self.assertEqual(Train.TRAIN_FULL, str(ve.exception))

    def test_add_passenger_successfully(self):
        self.train.add("Borislav")
        result = self.train.add("Neno")

        self.assertEqual(["Borislav", "Neno"], self.train.passengers)
        self.assertEqual(Train.PASSENGER_ADD.format("Neno"), result)

    def test_remove_passenger_with_invalid_input_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Borislav")

        self.assertEqual(Train.PASSENGER_NOT_FOUND, str(ve.exception))

    def test_remove_passenger_with_valid_input(self):
        self.train.add("Borislav")
        self.train.add("Blagovest")
        result = self.train.remove("Borislav")

        self.assertEqual(Train.PASSENGER_REMOVED.format("Borislav"), result)


if __name__ == "__main__":
    main()