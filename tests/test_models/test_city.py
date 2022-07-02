#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City
"""
Unittest for class City
"""


class TestCity(unittest.TestCase):
    """Testing with unittest"""
    def test_validate_format(self):
        """
        Test to validate the format that is string
        """
        city1 = City()
        self.assertIsInstance(city1.name, str)
        self.assertIsInstance(city1.state_id, str)

    def test_City_is_Subclass(self):
        """
        Test for BaseModel subclasses
        """
        city2 = City()
        cl = city2.__class__
        self.assertTrue(issubclass(cl, BaseModel))

    def test_empty_string(self):
        """
        Test to validate if it is empty
        """
        city3 = City()
        self.assertEqual(city3.name, "")
        self.assertEqual(city3.state_id, "")

    def test_representation_state(self):
        """
        Test to validate the representation of the User class
        """
        city4 = City()
        dictionary = city4.__dict__
        format_representation = "[{}] ({}) {}".format(city4.__class__.__name__,
                                                      city4.id, dictionary)
        self.assertEqual(format_representation, str(city4))

    def test_create_City(self):
        """
        Test to validate user creation
        """
        city5 = City()
        city5.name = "San Diego"
        city5.state_id = "613-29-5287"
        self.assertEqual(city5.name, "San Diego")
        self.assertEqual(city5.state_id, "613-29-5287")

    def test_create_update_City(self):
        """
        Test to validate the attribute value change update.
        """
        city6 = City()
        first = city6.name = "San Diego"
        city6.state_id = "613-29-5285"
        city6.save()
        second = city6.name = "New Mexico"
        city6.save()
        self.assertNotEqual(first, second)
