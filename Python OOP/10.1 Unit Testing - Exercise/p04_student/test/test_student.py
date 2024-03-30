import unittest
from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.student = Student("New Student",
                              {"Python": ["Basics", "Fundamentals"],
                               "Mathematics": ["Algebra"]})

    def test_student_initialization_no_courses(self):
        student = Student("Student")
        self.assertEqual("Student", student.name)
        self.assertEqual({}, student.courses)

    def test_student_initialization_with_courses(self):
        self.assertEqual("New Student", self.student.name)
        self.assertEqual({"Python": ["Basics", "Fundamentals"], "Mathematics": ["Algebra"]}, self.student.courses)

    def test_enroll_method_already_added_course_no_notes(self):
        result = self.student.enroll("Python", [])

        self.assertEqual("Course already added. Notes have been updated.", result)

        self.assertEqual({"Python": ["Basics", "Fundamentals"],
                          "Mathematics": ["Algebra"]}, self.student.courses)

    def test_enroll_method_already_added_course_with_new_notes(self):
        result = self.student.enroll("Python", ["Advanced", "OOP"])

        self.assertEqual("Course already added. Notes have been updated.", result)

        self.assertEqual({"Python": ["Basics", "Fundamentals", "Advanced", "OOP"],
                          "Mathematics": ["Algebra"]}, self.student.courses)

    def test_enroll_method_add_course_and_with_add_course_notes_as_param_char_y(self):
        result = self.student.enroll("Java", ["Basics"], "Y")
        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({"Python": ["Basics", "Fundamentals"],
                          "Mathematics": ["Algebra"], "Java": ["Basics"]}, self.student.courses)

    def test_enroll_method_add_course_and_with_add_course_notes_as_param_empty_string(self):
        result = self.student.enroll("Java", ["Basics"])
        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({"Python": ["Basics", "Fundamentals"],
                          "Mathematics": ["Algebra"], "Java": ["Basics"]}, self.student.courses)

    def test_enroll_method_add_course_with_other_add_notes_param(self):
        result = self.student.enroll("Java", ["Basics"], "N")
        self.assertEqual("Course has been added.", result)

        self.assertEqual({"Python": ["Basics", "Fundamentals"],
                          "Mathematics": ["Algebra"], "Java": []}, self.student.courses)

    def test_add_notes_method_existing_course(self):
        result = self.student.add_notes("Python", "Advanced")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"Python": ["Basics", "Fundamentals", "Advanced"],
                          "Mathematics": ["Algebra"]}, self.student.courses)

    def test_add_notes_method_non_existing_course_exception(self):
        result = None
        with self.assertRaises(Exception) as ex:
            result = self.student.add_notes("Java", "Spring Web")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertIsNone(result)
        self.assertEqual({"Python": ["Basics", "Fundamentals"],
                          "Mathematics": ["Algebra"]}, self.student.courses)

    def test_leave_course_method_existing_course(self):
        result = self.student.leave_course("Mathematics")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({"Python": ["Basics", "Fundamentals"]}, self.student.courses)

    def test_leave_course_method_non_existing_course_exception(self):
        result = None
        with self.assertRaises(Exception) as ex:
            result = self.student.leave_course("Java")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertIsNone(result)
        self.assertEqual({"Python": ["Basics", "Fundamentals"],
                          "Mathematics": ["Algebra"]}, self.student.courses)


if __name__ == "__main__":
    unittest.main()
