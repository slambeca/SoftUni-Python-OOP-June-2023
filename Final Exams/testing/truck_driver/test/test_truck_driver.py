from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTests(TestCase):
    def setUp(self):
        self.truck_driver = TruckDriver("Borislav", 1.00)

    def test_correct_initializing_of_truck_driver(self):
        self.assertEqual("Borislav", self.truck_driver.name)
        self.assertEqual(1, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_earned_money_setter_with_negative_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1

        self.assertEqual("Borislav went bankrupt.", str(ve.exception))

    def test_add_cargo_location_invalid_raise_exception(self):
        self.truck_driver.add_cargo_offer("Ruse", 300)

        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Ruse", 300)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_location_valid(self):
        result = self.truck_driver.add_cargo_offer("Ruse", 300)

        self.assertEqual("Cargo for 300 to Ruse was added as an offer.", result)
        self.assertEqual({"Ruse": 300}, self.truck_driver.available_cargos)

    def test_invalid_get_best_cargo_offer_raise_value_error(self):
        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)

    def test_valid_get_best_cargo_offer(self):
        self.truck_driver.add_cargo_offer("Sofia", 1000)
        self.truck_driver.add_cargo_offer("Ruse", 300)

        result = self.truck_driver.drive_best_cargo_offer()

        self.assertEqual("Borislav is driving 1000 to Sofia.", result)
        self.assertEqual(875, self.truck_driver.earned_money)
        self.assertEqual(1000, self.truck_driver.miles)

    def test_eat_activity(self):
        self.truck_driver.earned_money = 20
        self.truck_driver.eat(500)

        self.assertEqual(0, self.truck_driver.earned_money)

    def test_sleep_activity(self):
        self.truck_driver.earned_money = 45
        self.truck_driver.sleep(2000)

        self.assertEqual(0, self.truck_driver.earned_money)

    def test_pump_gas_activity(self):
        self.truck_driver.earned_money = 500
        self.truck_driver.pump_gas(1500)

        self.assertEqual(0, self.truck_driver.earned_money)

    def test_repair_truck_activity(self):
        self.truck_driver.earned_money = 7500
        self.truck_driver.repair_truck(10000)

        self.assertEqual(0, self.truck_driver.earned_money)

    def test__repr__valid(self):
        self.assertEqual("Borislav has 0 miles behind his back.", str(self.truck_driver))


if __name__ == "__main__":
    main()