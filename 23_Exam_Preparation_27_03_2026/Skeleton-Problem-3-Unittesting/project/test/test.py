from project.furniture import Furniture
from unittest import TestCase, main

class FurnitureTest(TestCase):
    def test_valid_initialization_default_values(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60)
        )
        self.assertEqual(furniture.model, "Table")
        self.assertEqual(furniture.price, 199.99)
        self.assertEqual(furniture.dimensions, (80, 120, 60))
        self.assertTrue(furniture.in_stock)
        self.assertIsNone(furniture.weight)

    def test_valid_initialization_with_passed_values(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            False,
            15.5
        )

        self.assertEqual(furniture.model, "Table")
        self.assertEqual(furniture.price, 199.99)
        self.assertEqual(furniture.dimensions, (80, 120, 60))
        self.assertFalse(furniture.in_stock)
        self.assertEqual(furniture.weight, 15.5)


    def test_invalid_model(self):
        with self.assertRaises(ValueError) as err:
            Furniture("", 199.99, (80, 120, 60))

        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(err.exception))

        with self.assertRaises(ValueError) as err:
            Furniture("" * 50, 199.99, (80, 120, 60))

        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(err.exception))


    def test_invalid_model_more_than_50(self):
        with self.assertRaises(ValueError) as err:
            Furniture("T" * 51, 199.99, (80, 120, 60))

        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.", str(err.exception))


    def test_invalid_price(self):
        with self.assertRaises(ValueError) as err:
            Furniture("Table", -199.99, (80, 120, 60))
        self.assertEqual("Price must be a non-negative number.", str(err.exception))


    def test_invalid_dimensions__less_than_3_elements(self):
        with self.assertRaises(ValueError) as err:
            Furniture("Table", 199.99, (80, 120))
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(err.exception))


    def test_invalid_dimensions__negative_value_element(self):
        with self.assertRaises(ValueError) as err:
            Furniture("Table", 199.99, (80, -120, 60))
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(err.exception))


    def test_invalid_dimensions__zero_value_element(self):
        with self.assertRaises(ValueError) as err:
            Furniture("Table", 199.99, (80, 0, 60))
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(err.exception))

        with self.assertRaises(ValueError) as err:
            Furniture("Table", 199.99, (0, 0, 0))
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(err.exception))


    def test_invalid_weight__value_negative(self):
        furniture = Furniture("Table", 199.99, (80, 120, 60))

        with self.assertRaises(ValueError) as err:
            furniture.weight = -0.01

        self.assertEqual("Weight must be greater than zero.", str(err.exception))


    def test_invalid_weight__zero(self):
        furniture = Furniture("Table", 199.99, (80, 120, 60))

        with self.assertRaises(ValueError) as err:
            furniture.weight = 0.00

        self.assertEqual("Weight must be greater than zero.", str(err.exception))


    def test_invalid_weight__passing_None(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            True,
            None
        )
        self.assertIsNone(furniture.weight)


    def test_valid_get_available_status__available(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60)
        )

        self.assertEqual("Model: Table is currently in stock.", furniture.get_available_status())


    def test_valid_get_available_status__unavailable(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            False
        )

        self.assertEqual("Model: Table is currently unavailable.", furniture.get_available_status())


    def test_get_specifications__with_weight(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            True,
            15.5
        )

        self.assertEqual("Model: Table has the following dimensions: 80mm x 120mm x 60mm and weighs: 15.5" ,furniture.get_specifications())


    def test_get_specifications__no_weight(self):
        furniture = Furniture(
            "Table",
            199.99,
            (80, 120, 60),
            True,
            None
        )

        self.assertEqual("Model: Table has the following dimensions: 80mm x 120mm x 60mm and weighs: N/A",
                         furniture.get_specifications())


if __name__ == "__main__":
    main()
