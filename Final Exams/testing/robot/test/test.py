from unittest import TestCase, main
from project.robot import Robot


class RobotTests(TestCase):
    def setUp(self):
        self.robot = Robot("1", "Military", 10, 100)
        self.new_robot = Robot("2", "Education", 10, 90)

    def test_default_class_attributes(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], Robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, Robot.PRICE_INCREMENT)

    def test_correct_initializing(self):
        self.assertEqual("1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(100, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_incorrect_category_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Maid"

        self.assertEqual(f"Category should be one of '{Robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_correct_category(self):
        self.assertEqual("Military", self.robot.category)

    def test_incorrect_price_cannot_be_less_than_zero_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_correct_price(self):
        self.assertEqual(100, self.robot.price)

    def test_unsuccessful_upgrade_with_return(self):
        self.robot.hardware_upgrades.append("RAM")
        result = self.robot.upgrade("RAM", 50)
        self.assertEqual(f"Robot 1 was not upgraded.", result)

    def test_successful_upgrade_with_return(self):
        result = self.robot.upgrade("GPU", 50)
        self.assertEqual(["GPU"], self.robot.hardware_upgrades)
        self.assertEqual(175, self.robot.price)
        self.assertEqual("Robot 1 was upgraded with GPU.", result)

    def test_update_not_existing_version_and_enough_capacity_should_update_successfully(self):
        result = self.robot.update(2.22, 5)
        self.assertEqual([2.22], self.robot.software_updates)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual("Robot 1 was updated to version 2.22.", result)

    def test_update_existing_version_and_enough_capacity_should_not_update(self):
        self.robot.software_updates.append(2.22)
        result = self.robot.update(2.22, 5)
        self.assertEqual("Robot 1 was not updated.", result)

    def test_update_lower_version_and_enough_capacity_should_not_update(self):
        self.robot.software_updates.append(2.22)
        result = self.robot.update(2.20, 5)
        self.assertEqual("Robot 1 was not updated.", result)

    def test__gt__method_between_two_robots_first_is_more_expensive(self):
        result = self.robot > self.new_robot
        self.assertEqual(result, "Robot with ID 1 is more expensive than Robot with ID 2.")

    def test__gt__method_between_two_robots_with_same_price(self):
        self.new_robot.price = 100
        result = self.robot > self.new_robot
        self.assertEqual(result, "Robot with ID 1 costs equal to Robot with ID 2.")

    def test__gt__method_between_two_robots_first_is_cheaper(self):
        self.new_robot.price = 120
        result = self.robot > self.new_robot
        self.assertEqual(result, "Robot with ID 1 is cheaper than Robot with ID 2.")


if __name__ == "__main__":
    main()