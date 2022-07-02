#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
"""
Unittest for class Amenity
"""


class TestAmenity(unittest.TestCase):
    """Testing with unittest"""
    def test_validate_format(self):
        """
        Test to validate the format that is string
        """
        amenity1 = Amenity()
        self.assertIsInstance(amenity1.name, str)

    def test_Amenity_is_Subclass(self):
        """
        Test for BaseModel subclasses
        """
        amenity2 = Amenity()
        cl = amenity2.__class__
        self.assertTrue(issubclass(cl, BaseModel))

    def test_empty_string(self):
        """
        Test to validate if it is empty
        """
        amenity3 = Amenity()
        self.assertEqual(amenity3.name, "")

    def test_representation_state(self):
        """
        Test to validate the representation of the User class
        """
        amenity4 = Amenity()
        dictionary = amenity4.__dict__
        format_representation = "[{}] ({}) {}".format(amenity4.__class__.__name__,
                                                      amenity4.id, dictionary)
        self.assertEqual(format_representation, str(amenity4))    

    def test_create_Amenity(self):
        """
        Test to validate user creation
        """
        amenity5 = Amenity()
        amenity5.name = "hot tub"
        self.assertEqual(amenity5.name, "hot tub")

    def test_create_update_Amenity(self):
        """
        Test to validate the attribute value change update.
        """
        amenity6 = Amenity()
        first = amenity6.name = "jacuzzi"
        amenity6.save()
        second = amenity6.name = "another room"
        amenity6.save()
        self.assertNotEqual(first, second)
