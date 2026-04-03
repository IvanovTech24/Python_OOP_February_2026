from project.senior_student import SeniorStudent
from unittest import TestCase, main


class SeniorStudentTest(TestCase):
    def setUp(self):
        self.student = SeniorStudent("2747", "Ivan", 5.8)

    def test_init(self):
        self.assertEqual(self.student.student_id, "2747")
        self.assertEqual(self.student.name, "Ivan")
        self.assertEqual(self.student.student_gpa, 5.8)
        self.assertEqual(self.student.colleges, set())


    def test_student_id_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_id = "2"
        self.assertEqual("Student ID must be at least 4 digits long!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.student.student_id = ""
        self.assertEqual("Student ID must be at least 4 digits long!", str(ve.exception))


    def test_name_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.student.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(ve.exception))


    def test_student_gpa_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_gpa = -2.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.student.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ve.exception))


    def test_apply_to_college__fail_low_gpa(self):
        gpa_required = 6.0
        college_name = "Harvard"
        result = self.student.apply_to_college(gpa_required, college_name)
        self.assertEqual("Application failed!", result)
        self.assertEqual(self.student.colleges, set())


    def test_apply_to_college__success(self):
        gpa_required = 5.0
        college_name = "Harvard"
        result = self.student.apply_to_college(gpa_required, college_name)
        self.assertEqual("Ivan successfully applied to Harvard.", result)
        self.assertEqual({"HARVARD"}, self.student.colleges)


    def test_update_gpa__with_valid_gpa(self):
        new_gpa = 5.0
        result = self.student.update_gpa(new_gpa)
        self.assertEqual(self.student.student_gpa, new_gpa)
        self.assertEqual("Student GPA was successfully updated.", result)


    def test_update_gpa__with_invalid_gpa(self):
        new_gpa = 1.0
        result = self.student.update_gpa(new_gpa)
        self.assertEqual("The GPA has not been changed!", result)

        new_gpa = -1.0
        result = self.student.update_gpa(new_gpa)
        self.assertEqual("The GPA has not been changed!", result)


    def test_eq_same_gpa(self):
        student2 = SeniorStudent("87548", "Petar", 5.8)
        self.assertTrue(self.student == student2)


    def test_eq_different_gpa(self):
        student2 = SeniorStudent("87548", "Petar", 3.8)
        self.assertFalse(self.student == student2)




if __name__ == "__main__":
    main()
