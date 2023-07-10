from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TennisPlayerTests(TestCase):
    def setUp(self):
        self.tennis_player = TennisPlayer("Borislav", 33, 100)
        self.other_tennis_player = TennisPlayer("Blagovest", 34, 50)

    def test_correct_initializing_of_instances(self):    # No need to check the second player initializing
        self.assertEqual("Borislav", self.tennis_player.name)
        self.assertEqual(33, self.tennis_player.age)
        self.assertEqual(100, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_check_for_invalid_name_raise_value_error(self):    # The correct name initializing is already checked above
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "Bo"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_check_for_invalid_age_raise_value_error(self):    # The correct age initializing is already checked above
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_try_to_add_already_added_win_to_wins(self):
        win = "Wimbledon"
        self.tennis_player.wins = [win]

        result = self.tennis_player.add_new_win(win)
        self.assertEqual(f"{win} has been already added to the list of wins!", result)

    def test_try_to_add_unique_win_to_wins(self):
        self.tennis_player.add_new_win("Wimbledon")
        self.tennis_player.add_new_win("Roland Garros")
        self.assertEqual(["Wimbledon", "Roland Garros"], self.tennis_player.wins)

    def test__lt__first_player_more_points_than_second(self):
        result = self.tennis_player.__lt__(self.other_tennis_player)
        self.assertEqual(f'Borislav is a better player than Blagovest', result)

    def test__lt__second_player_more_points_than_first(self):
        self.other_tennis_player.points = 150
        result = self.tennis_player.__lt__(self.other_tennis_player)
        self.assertEqual(f'Blagovest is a top seeded player and he/she is better than Borislav', result)

    def test_correct__str__with_no_wins(self):
        result = str(self.tennis_player)
        expected_result = f"Tennis Player: Borislav\nAge: 33\nPoints: 100.0\nTournaments won: "

        self.assertEqual(result, expected_result)

    def test_correct_str_with_two_wins(self):
        self.tennis_player.wins.append("Wimbledon")
        self.tennis_player.wins.append("Roland Garros")
        result = str(self.tennis_player)
        expected_result = f"Tennis Player: Borislav\nAge: 33\nPoints: 100.0\nTournaments won: Wimbledon, Roland Garros"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()