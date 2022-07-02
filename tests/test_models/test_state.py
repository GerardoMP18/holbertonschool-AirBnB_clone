#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State
"""
Unittest for class State
"""


class TestState(unittest.TestCase):
    """Testing with unittest"""
    def test_validate_format(self):
        """
        Test to validate the format that is string
        """
        state1 = State()
        self.assertIsInstance(state1.name, str)

    def test_State_is_Subclass(self):
        """
        Test for BaseModel subclasses
        """
        state2 = State()
        cl = state2.__class__
        self.assertTrue(issubclass(cl, BaseModel))

    def test_empty_string(self):
        """
        Test to validate if it is empty
        """
        state3 = State()
        self.assertEqual(state3.name, "")

    def test_representation_state(self):
        """
        Test to validate the representation of the User class
        """
        state4 = State()
        dictionary = state4.__dict__
        format_representation = "[{}] ({}) {}".format(
                state4.__class__.__name__, state4.id, dictionary)
        self.assertEqual(format_representation, str(state4))

    def test_create_State(self):
        """
        Test to validate user creation
        """
        state5 = State()
        state5.name = "California"
        self.assertEqual(state5.name, "California")

    def test_create_update_State(self):
        """
        Test to validate the attribute value change update.
        """
        state6 = State()
        first = state6.name = "Florida"
        state6.save()
        second = state6.name = "Illinois"
        state6.save()
        self.assertNotEqual(first, second)
