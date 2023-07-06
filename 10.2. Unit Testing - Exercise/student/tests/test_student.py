from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student("TestGuy1")
        self.student_with_course = Student("TestGuy2", {"math": ["note"]})

    def test_correct_initializing(self):
        self.assertEqual("TestGuy1", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["note"]}, self.student_with_course.courses)

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.enroll("math", ["first note", "second note"])
        self.assertEqual(["note", "first note", "second note"], self.student_with_course.courses["math"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_notes_to_non_existing_course_without_third_param(self):
        result = self.student.enroll("python", ["python is really cool"])

        self.assertEqual(["python is really cool"], self.student.courses["python"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_notes_to_non_existing_course_with_third_param_Y(self):
        result = self.student.enroll("python", ["python is really cool"], "Y")

        self.assertEqual(["python is really cool"], self.student.courses["python"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_new_course_without_adding_the_notes(self):
        result = self.student.enroll("python", ["python is really cool"], "n")

        self.assertEqual([], self.student.courses["python"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_on_existing_course(self):
        result = self.student_with_course.add_notes("math", "that's a new note")
        self.assertEqual(["note", "that's a new note"], self.student_with_course.courses["math"])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("math", "some note")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("math")

        self.assertEqual({}, self.student_with_course.courses)
        self.assertEqual("Course has been removed", result)

    def test_leaving_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()