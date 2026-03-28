from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    fuel = 37.5
    horse_power = 127.8

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertTrue(isinstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))


    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)


    def test_drive_success(self):
        self.vehicle.drive(5)
        self.assertEqual(31.25, self.vehicle.fuel)


    def test_drive_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))



    def test_refuel_success(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(1.8)
        self.assertEqual(2.8, self.vehicle.fuel)


    def test_refuel_raises_too_much_fuel_exception(self):
        self.vehicle.fuel = 30
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(17.7)
        self.assertEqual("Too much fuel", str(ex.exception))


    def test_str(self):
        expected = (f"The vehicle has {self.horse_power} "
                    f"horse power with {self.fuel} fuel left "
                    f"and 1.25 fuel consumption")
        self.assertEqual(expected, str(self.vehicle))



if __name__ == "__main__":
    main()