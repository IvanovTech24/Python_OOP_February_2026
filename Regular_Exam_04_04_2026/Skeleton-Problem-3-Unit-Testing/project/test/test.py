from project.star_system import StarSystem
from unittest import TestCase, main


class StarSystemTest(TestCase):
    def setUp(self):
        self.system = StarSystem("Alpha", "Red dwarf", "Single", 3, (0.5, 1.5))


    def test_init(self):
        self.assertEqual(self.system.name, "Alpha")
        self.assertEqual(self.system.star_type, "Red dwarf")
        self.assertEqual(self.system.system_type, "Single")
        self.assertEqual(self.system.num_planets, 3)
        self.assertEqual(self.system.habitable_zone_range, (0.5, 1.5))


    def test_name_validation__with_empty_value(self):
        with self.assertRaises(ValueError) as ve:
            self.system.name = "   "
        self.assertEqual(str(ve.exception), "Name must be a non-empty string.")


    def test_star_type__with_invalid_type(self):
        invalid_type = "Supernova"
        with self.assertRaises(ValueError) as ve:
            self.system.star_type = invalid_type
        self.assertIn("Star type must be one of", str(ve.exception))

    def test_system_type_validation(self):
        self.system.system_type = "Binary"
        self.assertEqual(self.system.system_type, "Binary")

    def test_system_type__with_invalid_type(self):
        invalid_system = "Galaxy Cluster"
        with self.assertRaises(ValueError) as ve:
            self.system.system_type = invalid_system

        expected_msg = f"System type must be one of {sorted(self.system._STAR_SYSTEM_TYPES)}."
        self.assertEqual(str(ve.exception), expected_msg)



    def test_num_planets__with_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.system.num_planets = -1
        self.assertEqual(str(ve.exception), "Number of planets must be a non-negative integer.")

    def test_habitable_zone_range__with_invalid_data(self):
        with self.assertRaises(ValueError) as ve:
            self.system.habitable_zone_range = (1.0,)
        self.assertIn("Habitable zone range must be a tuple of two numbers", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.system.habitable_zone_range = (2.0, 1.0)
        self.assertIn("where start < end", str(ve.exception))

    def test_is_habitable_validation(self):
        self.assertTrue(self.system.is_habitable)

        self.system.num_planets = 0
        self.assertFalse(self.system.is_habitable)

        self.system.num_planets = 5
        self.system.habitable_zone_range = None
        self.assertFalse(self.system.is_habitable)

    def test_gt_validation__not_habitable(self):
        other = StarSystem("Beta", "Blue giant", "Binary", 0)  # Не е обитаема (0 планети)
        with self.assertRaises(ValueError) as ve:
            result = self.system > other
        self.assertEqual(str(ve.exception),
                         "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_gt_with_correct_value(self):
        other = StarSystem("Beta", "Blue giant", "Binary", 2, (1.0, 1.2))
        self.assertTrue(self.system > other)

        smaller_range_system = StarSystem("Gamma", "Yellow dwarf", "Single", 1, (1.0, 3.0))
        self.assertFalse(self.system > smaller_range_system)

    def test_compare_star_systems(self):
        other = StarSystem("Beta", "Blue giant", "Binary", 2, (1.0, 1.2))

        res = StarSystem.compare_star_systems(self.system, other)
        self.assertEqual(res, "Alpha has a wider habitable zone than Beta.")

        res2 = StarSystem.compare_star_systems(other, self.system)
        self.assertEqual(res2, "Alpha has a wider or equal habitable zone compared to Beta.")

    def test_compare_star_systems_exception(self):
        other = StarSystem("Empty", "Red dwarf", "Single", 0)  # No planets
        res = StarSystem.compare_star_systems(self.system, other)
        self.assertEqual(res, "Comparison not possible: One or both systems lack a defined habitable zone or planets.")


if __name__ == "__main__":
    main()
