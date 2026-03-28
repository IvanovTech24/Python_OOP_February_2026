from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "Test type", "test sound")

    def test_init(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("Test type", self.mammal.type)
        self.assertEqual("test sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)


    def test_make_sound(self):
        actual = self.mammal.make_sound()
        self.assertEqual("Test makes test sound", actual)


    def test_get_kingdom(self):
        actual = self.mammal.get_kingdom()
        self.assertEqual("animals", actual)


    def test_info(self):
        actual = self.mammal.info()
        self.assertEqual("Test is of type Test type", actual)


if __name__ == "__main__":
    main()