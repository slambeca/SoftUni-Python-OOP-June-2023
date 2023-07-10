from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTests(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_correct_initializing(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_check_invalid_size_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_check_hire_but_worker_is_already_hired_raise_value_error(self):
        self.plantation.hire_worker("Jesus")

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Jesus")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_check_hire_worker_correctly(self):
        result = self.plantation.hire_worker("Jesus")

        self.assertEqual("Jesus successfully hired.", result)

    def test_correct__len__method(self):
        self.plantation.hire_worker("Jesus")
        self.plantation.hire_worker("Blagovest")
        self.plantation.planting("Jesus", "Rose")
        self.plantation.planting("Blagovest", "Tulip")
        self.plantation.planting("Jesus", "Tulip")

        total_sum = 0
        for key, value in self.plantation.plants.items():
            total_sum += len(value)

        self.assertEqual(3, total_sum)

    def test_planting_with_invalid_worker_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Jesus", "Rose")

        self.assertEqual("Worker with name Jesus is not hired!", str(ve.exception))

    def test_planting_with_not_sufficient_size_raise_value_error(self):
        self.plantation.size = 2
        self.plantation.hire_worker("Jesus")
        self.plantation.hire_worker("Blagovest")
        self.plantation.planting("Jesus", "Rose")
        self.plantation.planting("Blagovest", "Tulip")

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Jesus", "Some flower")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_with_sufficient_size_and_correct_worker(self):
        self.plantation.hire_worker("Jesus")
        result = self.plantation.planting("Jesus", "Rose")

        self.assertEqual("Jesus planted it's first Rose.", result)

    def test_planting_with_sufficient_size_and_correct_worker_again(self):
        self.plantation.hire_worker("Jesus")
        self.plantation.planting("Jesus", "Rose")
        result = self.plantation.planting("Jesus", "Rose")

        self.assertEqual("Jesus planted Rose.", result)

    def test_correct__str__method_with_workers_and_plants(self):
        self.plantation.hire_worker("Jesus")
        self.plantation.hire_worker("Blagovest")
        self.plantation.planting("Jesus", "Rose")
        self.plantation.planting("Blagovest", "Tulip")
        result = str(self.plantation)
        expected_result = "Plantation size: 10\nJesus, Blagovest\nJesus planted: Rose\nBlagovest planted: Tulip"

        self.assertEqual(result, expected_result)

    def test_correct__repr__method(self):
        self.plantation.hire_worker("Jesus")
        self.plantation.hire_worker("Blagovest")
        result = repr(self.plantation)
        expected_result = "Size: 10\nWorkers: Jesus, Blagovest"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()