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

    def test_creation_new_instance(self):
        """
        Test to validate that the attribute is equal to the input
        """
        base9 = BaseModel()
        base9.name = "gerardo"
        base9.my_number = 89
        base9.save()
        self.assertEqual(base9.name, "gerardo")
        self.assertEqual(base9.my_number, 89)

    def test_creation_update_diferent(self):
        """
        Test to validate that the creation of the date is
        different in different instances.
        """
        base10 = BaseModel()
        base10.name = "Dhana"
        base10.my_number = 20
        base10.save()
        base11 = BaseModel()
        base11.name = "Ghueral"
        base11.my_number = 14
        base11.save()
        self.assertNotEqual(base10.created_at, base11.created_at)
        self.assertNotEqual(base10.updated_at, base11.updated_at)

    def test_to_dict(self):
        """
        Test to validate that the key is in the instance.
        """
        base12 = BaseModel()
        dictionary_value = base12.to_dict()
        self.assertIn('__class__', dictionary_value)
        self.assertIn('created_at', dictionary_value)
        self.assertIn('updated_at', dictionary_value)
        self.assertIn('id', dictionary_value)

    def test_kwargs(self):
        """
        Test kwarg by passing the keywords
        """
        dictionary_json = {'id': '33448c92-6b9d-4f56-8b27-d8a4a0e9be72',
                           'created_at': '2022-07-02T10:46:04.535249',
                           'updated_at': '2022-07-02T10:46:04.535517',
                           'name': 'My First Model',
                           'my_number': 89,
                           '__class__': 'BaseModel'}
        base13 = BaseModel(**dictionary_json)
        nameclass = base13.__class__.__name__
        format_date = '\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}.\\d{6}'
        self.assertEqual(nameclass, "BaseModel")
        self.assertEqual(len(base13.id), 36)
        self.assertNotEqual(base13.id, None)
        self.assertIsInstance(base13.id, str)
        self.assertIsInstance(base13.created_at, datetime)
        self.assertIsInstance(base13.updated_at, datetime)
        self.assertRegex(str(base13.created_at), format_date)
        self.assertRegex(str(base13.updated_at), format_date)
        self.assertEqual(base13.name, 'My First Model')
        self.assertEqual(base13.my_number, 89)

    def test_update_basemodel(self):
        """
        Test to validate the update change that in the date and value
        """
        base14 = BaseModel()
        base14.name = "gerardo"
        first = base14.my_number = 974133101
        first_date = base14.updated_at
        base14.save()
        second = base14.my_number = 943136201
        second_date = base14.updated_at
        base14.save()
        self.assertNotEqual(first, second)
        self.assertNotEqual(first_date, second_date)
