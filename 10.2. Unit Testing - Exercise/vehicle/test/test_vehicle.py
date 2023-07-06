from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.5, 175.5)

    def test_default_fuel_consumption_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_proper_initializing(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_without_enough_fuel_raise_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_valid_distance_expect_fuel_amount_reduce(self):
        self.vehicle.drive(1)

        self.assertEqual(19.25, self.vehicle.fuel)

    def test_refuel_with_greater_value_than_possible_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_valid_value(self):
        self.vehicle.fuel -= 1
        self.vehicle.refuel(1)
        self.assertEqual(20.50, self.vehicle.fuel)

    def test_correct__str__(self):
        result = str(self.vehicle)
        expected_result = f"The vehicle has 175.5 " \
               f"horse power with 20.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()