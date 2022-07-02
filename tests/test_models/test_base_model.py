#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
"""
Unittest for class Base Model
"""


class TestBase_model(unittest.TestCase):
    """Testing with unittest"""
    def test_unique_id(self):
        """
        Tests to validate that the ID code is different
        from the others created
        """
        Base1 = BaseModel()
        Base2 = BaseModel()
        self.assertNotEqual(Base1.id, Base2.id)

    def test_class_name(self):
        """
        Test to validate the class name according to the created
        instance
        """
        Base3 = BaseModel()
        self.assertEqual(Base3.__class__.__name__, "BaseModel")

    def test_format_date(self):
        """
        Tests to validate the date format in the created_at and
        update_at instance attributes
        """
        base4 = BaseModel()
        formatD = '\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}'
        self.assertRegex(str(base4.created_at), formatD)
        self.assertRegex(str(base4.updated_at), formatD)

    def test_id_null(self):
        """
        Tests to validate that the ID code is not None
        """
        base5 = BaseModel()
        self.assertNotEqual(self.id, None)

    def test_count_id(self):
        """
        Test to validate that the ID code must be 36
        digits long
        """
        base6 = BaseModel()
        self.assertEqual(len(base6.id), 36)

    def test_typeAttribute(self):
        """
        Test to validate the converted attribute type
        """
        base7 = BaseModel()
        self.assertIsInstance(base7.id, str)
        self.assertIsInstance(base7.created_at, datetime)
        self.assertIsInstance(base7.updated_at, datetime)

    def test_representation(self):
        """
        Test to validate the mandatory format of the class
        representation
        """
        base8 = BaseModel()
        dictionary = base8.__dict__
        format_representation = "[{}] ({}) {}".format(base8.__class__.__name__,
                                                      base8.id, dictionary)
        self.assertEqual(format_representation, str(base8))

    def test_representation_with_value(self):
        """
        Representation test adding the code and verify that
        it is the same value of the representation
        """
        base8 = BaseModel()
        base8.id = "2d09fbee-82be-4531-852f-2add6d6e4f23"
        result = "[BaseModel] (2d09fbee-82be-4531-852f-2add6d6e4f23)"
        self.assertTrue(result, base8.__str__)
