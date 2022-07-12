#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.place import Place
"""
Unittest for class Place
"""


class TestPlace(unittest.TestCase):
    """Testing with unittest"""
    def test_validate_format(self):
        """
        Test to validate the format that is string
        """
        place1 = Place()
        self.assertIsInstance(place1.city_id, str)
        self.assertIsInstance(place1.user_id, str)
        self.assertIsInstance(place1.name, str)
        self.assertIsInstance(place1.description, str)
        self.assertIsInstance(place1.number_rooms, int)
        self.assertIsInstance(place1.number_bathrooms, int)
        self.assertIsInstance(place1.max_guest, int)
        self.assertIsInstance(place1.price_by_night, int)
        self.assertIsInstance(place1.latitude, float)
        self.assertIsInstance(place1.longitude, float)
        self.assertIsInstance(place1.amenity_ids, list)

    def test_Place_is_Subclass(self):
        """
        Test for BaseModel subclasses
        """
        place2 = Place()
        cl = place2.__class__
        self.assertTrue(issubclass(cl, BaseModel))

    def test_empty_string(self):
        """
        Test to validate if it is empty
        """
        place3 = Place()
        self.assertEqual(place3.city_id, "")
        self.assertEqual(place3.user_id, "")
        self.assertEqual(place3.name, "")
        self.assertEqual(place3.description, "")
        self.assertEqual(place3.number_rooms, 0)
        self.assertEqual(place3.number_bathrooms, 0)
        self.assertEqual(place3.max_guest, 0)
        self.assertEqual(place3.price_by_night, 0)
        self.assertEqual(place3.latitude, 0.0)
        self.assertEqual(place3.longitude, 0.0)
        self.assertEqual(place3.amenity_ids, [])

    def test_representation_place(self):
        """
        Test to validate the representation of the User class
        """
        place4 = Place()
        dictionary = place4.__dict__
        format_representation = "[{}] ({}) {}".format(
                place4.__class__.__name__, place4.id, dictionary)
        self.assertEqual(format_representation, str(place4))

    def test_create_Place(self):
        """
        Test to validate user creation
        """
        place5 = Place()
        place5.city_id = "ChIJrTLr-GyuEmsRBfy61i59si0"
        place5.user_id = "Elmo"
        place5.name = "Holberton"
        place5.description = "Innovative"
        place5.number_rooms = "4"
        place5.number_bathrooms = "1"
        place5.max_guest = "28"
        place5.price_by_night = "60"
        place5.latitude = "-33.870775"
        place5.longitude = "151.199025"
        place5.amenity_ids = "hot tub, jacuzzi"
        place5.save()
        self.assertEqual(place5.city_id, "ChIJrTLr-GyuEmsRBfy61i59si0")
        self.assertEqual(place5.user_id, "Elmo")
        self.assertEqual(place5.name, "Holberton")
        self.assertEqual(place5.description, "Innovative")
        self.assertEqual(place5.number_rooms, "4")
        self.assertEqual(place5.number_bathrooms, "1")
        self.assertEqual(place5.max_guest, "28")
        self.assertEqual(place5.price_by_night, "60")
        self.assertEqual(place5.latitude, "-33.870775")
        self.assertEqual(place5.longitude, "151.199025")
        self.assertEqual(place5.amenity_ids, "hot tub, jacuzzi")

    def test_create_update_Place(self):
        """
        Test to validate the attribute value change update.
        """
        place6 = Place()
        place6.city_id = "ChIJrTLr-GyuEmsRBfy61i59si0"
        place6.user_id = "Paolo"
        place6.name = "Huaral"
        first = place6.description = "Perfect"
        place6.number_rooms = "1"
        place6.number_bathrooms = "1"
        place6.max_guest = "6"
        place6.price_by_night = "40"
        place6.latitude = "-33.870775"
        place6.longitude = "151.199025"
        first_amenity = place6.amenity_ids = "good music"
        place6.save()
        second = place6.description = "Sus"
        second_amenity = place6.amenity_ids = "nothing interesting"
        self.assertNotEqual(first, second)
        self.assertNotEqual(first_amenity, second_amenity)
