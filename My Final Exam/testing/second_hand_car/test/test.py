from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class SecondHandCarTests(TestCase):
    def setUp(self):
        self.second_hand_car = SecondHandCar("Ford", "Sedan", 500, 1000.0)

    def test_correct_initializing(self):
        self.assertEqual("Ford", self.second_hand_car.model)
        self.assertEqual("Sedan", self.second_hand_car.car_type)
        self.assertEqual(500, self.second_hand_car.mileage)
        self.assertEqual(1000.0, self.second_hand_car.price)
        self.assertEqual([], self.second_hand_car.repairs)

    def test_invalid_price_with_less_than_one_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 0.0

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_invalid_price_with_one_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.price = 1.0

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_invalid_mileage_with_less_than_one_hundred_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 50

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_invalid_mileage_with_one_hundred_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_set_promotional_price_with_greater_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(2000.0)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_with_the_same_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.second_hand_car.set_promotional_price(1000.0)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_correct_set_promotional_price_returns_string(self):
        result = self.second_hand_car.set_promotional_price(500.0)

        self.assertEqual(500.0, self.second_hand_car.price)
        self.assertEqual("The promotional price has been successfully set.", result)

    def test_need_repair_with_greater_price_returns_string(self):
        result = self.second_hand_car.need_repair(2500, "Change windshield")

        self.assertEqual("Repair is impossible!", result)
        self.assertEqual(1000.0, self.second_hand_car.price)

    def test_correct_repair_with_correct_price(self):
        result = self.second_hand_car.need_repair(500, "Change windshield")

        self.assertEqual(1500.0, self.second_hand_car.price)
        self.assertEqual(["Change windshield"], self.second_hand_car.repairs)
        self.assertEqual("Price has been increased due to repair charges.", result)

    def test_check_greater_than_with_different_car_type(self):
        self.other_second_hand_car = SecondHandCar("Honda", "Touring", 500, 2000.0)

        result = self.second_hand_car > self.other_second_hand_car

        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test_check_greater_than_with_same_car_type_and_higher_price(self):
        self.other_second_hand_car = SecondHandCar("Honda", "Sedan", 500, 2000.0)

        result = self.second_hand_car > self.other_second_hand_car

        self.assertEqual(False, result)

    def test_check_greater_than_with_same_car_type_and_lower_price(self):
        self.other_second_hand_car = SecondHandCar("Honda", "Sedan", 500, 500.0)

        result = self.second_hand_car > self.other_second_hand_car

        self.assertEqual(True, result)

    def test_correct_str_returns_string(self):
        result = str(self.second_hand_car)
        expected_result = f"""Model Ford | Type Sedan | Milage 500km
Current price: 1000.00 | Number of Repairs: 0"""

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()