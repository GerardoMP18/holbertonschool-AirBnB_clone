#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review
"""
Unittest for class Review
"""


class TestReview(unittest.TestCase):
    """Testing with unittest"""
    def test_validate_format(self):
        """
        Test to validate the format that is string
        """
        review1 = Review()
        self.assertIsInstance(review1.place_id, str)
        self.assertIsInstance(review1.user_id, str)
        self.assertIsInstance(review1.text, str)

    def test_review_is_Subclass(self):
        """
        Test for BaseModel subclasses
        """
        review2 = Review()
        cl = review2.__class__
        self.assertTrue(issubclass(cl, BaseModel))

    def test_empty_string(self):
        """
        Test to validate if it is empty
        """
        review3 = Review()
        self.assertEqual(review3.place_id, "")
        self.assertEqual(review3.user_id, "")
        self.assertEqual(review3.text, "")

    def test_representation_review(self):
        """
        Test to validate the representation of the User class
        """
        review4 = Review()
        dictionary = review4.__dict__
        format_representation = "[{}] ({}) {}".format(
                review4.__class__.__name__, review4.id, dictionary)
        self.assertEqual(format_representation, str(review4))

    def test_create_Review(self):
        """
        Test to validate user creation
        """
        review5 = Review()
        review5.place_id = "ChIJrTLr-GyuEmsRBfy61i59si0"
        review5.user_id = "fole"
        review5.text = "Amazing place"
        self.assertEqual(review5.place_id, "ChIJrTLr-GyuEmsRBfy61i59si0")
        self.assertEqual(review5.user_id, "fole")
        self.assertEqual(review5.text, "Amazing place")

    def test_create_update_Review(self):
        """
        Test to validate the attribute value change update.
        """
        review6 = Review()
        review6.place_id = "ChIJrTLr-GyuEmsRBfy6155si0"
        review6.name = "gura"
        first = review6.text = "Awful experience"
        review6.save()
        second = review6.text = "Wonderful experience"
        review6.save()
        self.assertNotEqual(first, second)
