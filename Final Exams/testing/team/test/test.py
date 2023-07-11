from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):
    def setUp(self):
        self.team = Team("NavySeals")
        self.other_team = Team("KozloduiNuclearBombs")

    def test_correct_initializing(self):
        self.assertEqual("NavySeals", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_check_name_if_is_alpha_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Navy Seals"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_single_member_to_members_dictionary(self):
        result = self.team.add_member(John=30)

        self.assertEqual("Successfully added: John", result)
        self.assertEqual({"John": 30}, self.team.members)

    def test_add_multiple_members_to_members_dictionary(self):
        result = self.team.add_member(John=30, Erica=20)

        self.assertEqual("Successfully added: John, Erica", result)
        self.assertEqual({"John": 30, "Erica": 20}, self.team.members)

    def test_add_the_same_member_twice(self):    # This is not tested by Judge
        self.team.add_member(John=30)
        self.team.add_member(John=30)

        self.assertEqual({"John": 30}, self.team.members)

    def test_remove_single_member_that_does_not_exist(self):
        self.team.add_member(John=30, Erica=20)
        result = self.team.remove_member("Neno")

        self.assertEqual("Member with name Neno does not exist", result)
        self.assertEqual({"John": 30, "Erica": 20}, self.team.members)

    def test_remove_single_member_that_exists(self):
        self.team.add_member(John=30, Erica=20)
        result = self.team.remove_member("Erica")

        self.assertEqual("Member Erica removed", result)
        self.assertEqual({"John": 30}, self.team.members)

    def test__gt__method_with_another_instance_first_one_is_greater(self):
        self.team.add_member(John=30)
        self.team.add_member(Erica=25)
        self.other_team.add_member(John=30)

        result = self.team > self.other_team
        self.assertEqual(True, result)

    def test__gt__method_with_another_instance_second_one_is_greater(self):
        self.team.add_member(John=30)
        self.other_team.add_member(Erica=25)
        self.other_team.add_member(John=30)

        result = self.team > self.other_team
        self.assertEqual(False, result)

    def test__len__method(self):
        self.team.add_member(John=30)
        self.team.add_member(Erica=25)
        result = len(self.team.members)

        self.assertEqual(2, result)

    def test_add_method_with_other_instance(self):
        self.team.add_member(John=30, Erica=20)
        self.other_team.add_member(Neno=35)

        result = self.team.__add__(self.other_team)

        self.assertEqual("NavySealsKozloduiNuclearBombs", result.name)
        self.assertEqual({"John": 30, "Erica": 20, "Neno": 35}, result.members)
        self.assertEqual(3, len(result))

    def test__str__method(self):
        self.team.add_member(John=30)
        self.team.add_member(Erica=25)

        result = str(self.team)

        self.assertEqual("Team name: NavySeals\nMember: John - 30-years old\nMember: Erica - 25-years old", result)


if __name__ == "__main__":
    main()