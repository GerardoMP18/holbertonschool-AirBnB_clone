#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.user import User
"""
Unittest for class User
"""


class TestUser(unittest.TestCase):
    """Testing with unittest"""
    def test_validate_format(self):
        """
        Test to validate the format that is string
        """
        user1 = User()
        self.assertIsInstance(user1.email, str)
        self.assertIsInstance(user1.password, str)
        self.assertIsInstance(user1.first_name, str)
        self.assertIsInstance(user1.last_name, str)

    def test_User_is_Subclass(self):
        """
        Test for BaseModel subclasses
        """
        user2 = User()
        cl = user2.__class__
        self.assertTrue(issubclass(cl, BaseModel))

    def test_empty_string(self):
        """
        Test to validate if it is empty
        """
        user3 = User()
        self.assertEqual(user3.email, "")
        self.assertEqual(user3.password, "")
        self.assertEqual(user3.first_name, "")
        self.assertEqual(user3.last_name, "")

    def test_representation_user(self):
        """
        Test to validate the representation of the User class
        """
        user4 = User()
        dictionary = user4.__dict__
        format_representation = "[{}] ({}) {}".format(user4.__class__.__name__,
                                                      user4.id, dictionary)
        self.assertEqual(format_representation, str(user4))

    def test_create_User(self):
        """
        Test to validate user creation
        """
        user5 = User()
        user5.email = "gerardomarinparra18@gmail.com"
        user5.password = "123456"
        user5.first_name = "Gerardo1"
        user5.last_name = "Marin"
        user5.save()
        self.assertEqual(user5.email, "gerardomarinparra18@gmail.com")
        self.assertEqual(user5.password, "123456")
        self.assertEqual(user5.first_name, "Gerardo1")
        self.assertEqual(user5.last_name, "Marin")

    def test_create_update_User(self):
        """
        Test to validate the attribute value change update.
        """
        user6 = User()
        user6.email = "dhannaps03@gmail.com"
        user6.password = "987654"
        first = user6.first_name = "Dhanna"
        user6.last_name = "Palomino"
        first_date = user6.updated_at
        user6.save()
        second = user6.password = "123456"
        second_date = user6.updated_at
        user6.save()
        self.assertNotEqual(first, second)
        self.assertNotEqual(first_date, second_date)
