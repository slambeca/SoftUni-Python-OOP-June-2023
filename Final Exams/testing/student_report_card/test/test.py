from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self):
        self.student_report_card = StudentReportCard("Borislav", 10)

    def test_correct_initializing(self):
        self.assertEqual("Borislav", self.student_report_card.student_name)
        self.assertEqual(10, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_correct_student_name_with_empty_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.student_name = ""

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_correct_school_year_with_zero_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student_report_card.school_year = 0

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_correct_school_year(self):
        self.student_report_card.school_year = 1

        self.assertEqual(1, self.student_report_card.school_year)

    def test_correct_school_year_twelve(self):
        self.student_report_card.school_year = 12

        self.assertEqual(12, self.student_report_card.school_year)

    def test_add_second_grade_method_with_valid_input(self):
        self.student_report_card.add_grade("Mathematics", 6.00)
        self.student_report_card.add_grade("Mathematics", 5.00)

        self.assertEqual({'Mathematics': [6.0, 5.0]}, self.student_report_card.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student_report_card.add_grade("Mathematics", 6.00)
        self.student_report_card.add_grade("Mathematics", 5.00)
        self.student_report_card.add_grade("Robotics", 6.00)
        self.student_report_card.add_grade("Robotics", 5.00)

        result = self.student_report_card.average_grade_by_subject()

        self.assertEqual("Mathematics: 5.50\nRobotics: 5.50", result)

    def test_average_grade_for_all_subjects(self):
        self.student_report_card.add_grade("Mathematics", 6.00)
        self.student_report_card.add_grade("Mathematics", 5.00)
        self.student_report_card.add_grade("Electronics", 6.00)
        self.student_report_card.add_grade("Electronics", 5.00)

        result = self.student_report_card.average_grade_for_all_subjects()

        self.assertEqual("Average Grade: 5.50", result)

    def test_correct__repr__method(self):
        self.student_report_card.add_grade("Mathematics", 6.00)
        self.student_report_card.add_grade("Mathematics", 5.00)
        self.student_report_card.add_grade("Electronics", 6.00)
        self.student_report_card.add_grade("Electronics", 5.00)
        result = repr(self.student_report_card)
        expected_result = "Name: Borislav\nYear: 10\n----------\nMathematics: 5.50\nElectronics: 5.50\n----------\n" \
                          "Average Grade: 5.50"

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()