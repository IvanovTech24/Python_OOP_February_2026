from project.gallery import Gallery
from unittest import TestCase, main


class GalleryTest(TestCase):
    def setUp(self):
        self.gallery = Gallery("Louvre", "Paris", 150000.5, True)

    def test_init(self):
        self.assertEqual(self.gallery.gallery_name, "Louvre")
        self.assertEqual(self.gallery.city, "Paris")
        self.assertEqual(self.gallery.area_sq_m, 150000.5)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual(self.gallery.exhibitions, {})

    def test_name_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.gallery_name = "Louvre! "
        self.assertEqual("Gallery name can contain letters and digits only!", str(ve.exception))


    def test_city_validation__not_value(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.city = ""
        self.assertEqual("City name must start with a letter!", str(ve.exception))


    def test_city_validation__starts_with_digit(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.city = "1Louvre"
        self.assertEqual("City name must start with a letter!", str(ve.exception))


    def test_area_sq_m_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.gallery.area_sq_m = -150000.5
        self.assertEqual("Gallery area must be a positive number!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.gallery.area_sq_m = 0.0
        self.assertEqual("Gallery area must be a positive number!", str(ve.exception))


    def test_add_exhibition_validation(self):
        self.assertEqual(len(self.gallery.exhibitions), 0)

        result = self.gallery.add_exhibition("Mona Lisa", 1503)

        self.assertEqual('Exhibition "Mona Lisa" added for the year 1503.', result)
        self.assertEqual(self.gallery.exhibitions["Mona Lisa"], 1503)

        existing_exhibition = self.gallery.add_exhibition("Mona Lisa", 1503)
        self.assertEqual('Exhibition "Mona Lisa" already exists.', existing_exhibition)


    def test_remove_exhibition_success(self):
        self.gallery.exhibitions = {
            "Mona Lisa": 1503,
            "La Liberté guidant le peuple": 1830
        }

        result = self.gallery.remove_exhibition("Mona Lisa")
        self.assertEqual('Exhibition "Mona Lisa" removed.', result)
        self.assertNotIn("Mona Lisa", self.gallery.exhibitions)



    def test_remove_exhibition_not_found(self):
        self.assertEqual(len(self.gallery.exhibitions), 0)
        result = self.gallery.remove_exhibition("Mona Lisa")
        self.assertEqual('Exhibition "Mona Lisa" not found.', result)


    def test_list_exhibitions__closed_gallery(self):
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        self.assertEqual('Gallery Louvre is currently closed for public! Check for updates later on.', result)

    def test_list_exhibitions__open_gallery(self):
        self.assertTrue(self.gallery.open_to_public)
        self.gallery.exhibitions = {
            "Mona Lisa": 1503
        }
        result = self.gallery.list_exhibitions()
        self.assertEqual("Mona Lisa: 1503", result)



if __name__ == "__main__":
    main()


