#!/usr/bin/python3
import unittest
from models .engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import os
"""
Unittest for class FileStorage
"""


class TestFileStorage(unittest.TestCase):
    """
    Testitng with unittest
    """

    def test_all(self):
        """
        test to validate the all
        """
        fStorage = FileStorage()
        dictionary_obj = fStorage.all()
        self.assertEqual(type(dictionary_obj), dict)

    def test_new_obj(self):
        """
        Test to validate a new method
        """
        for obj in models.storage.all().values():
            string = obj
        self.assertTrue(string is obj)

    def test_file_exists(self):
        """
        Test to validate if the file exists
        """
        os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))
        baseModel1 = BaseModel()
        baseModel1.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_save_BaseModel(self):
        """
        Test to validate that you save the instance in
        the json file with the BaseModel class
        """
        os.remove("file.json")
        baseModel2 = BaseModel()
        baseModel2.save()
        with open("file.json", "r") as myFile:
            readFile = myFile.read()
            string = "{}.{}".format(baseModel2.__class__.__name__,
                                    baseModel2.id)
            self.assertIn(string, readFile)

    def test_save_User(self):
        """
        Test to validate that you save the instance in
        the json file with the User class
        """
        os.remove("file.json")
        user1 = User()
        user1.save()
        with open("file.json", "r") as myFileUser:
            readFileUser = myFileUser.read()
            stringUser = "{}.{}".format(user1.__class__.__name__, user1.id)
            self.assertIn(stringUser, readFileUser)

    def test_save_State(self):
        """
        Test to validate that you save the instance in
        the json file with the State class
        """
        os.remove("file.json")
        state1 = State()
        state1.save()
        with open("file.json", "r") as myFileState:
            readFileState = myFileState.read()
            stringState = "{}.{}".format(state1.__class__.__name__, state1.id)
            self.assertIn(stringState, readFileState)

    def test_save_City(self):
        """
        Test to validate that you save the instance in
        the json file with the City class
        """
        os.remove("file.json")
        city1 = City()
        city1.save()
        with open("file.json", "r") as myFileCity:
            readFileCity = myFileCity.read()
            stringCity = "{}.{}".format(city1.__class__.__name__, city1.id)
            self.assertIn(stringCity, readFileCity)

    def test_save_Amenity(self):
        """
        Test to validate that you save the instance in
        the json file with the Amenity class
        """
        os.remove("file.json")
        amenity1 = Amenity()
        amenity1.save()
        with open("file.json", "r") as myFileAmenity:
            readFileAmenity = myFileAmenity.read()
            stringAmenity = "{}.{}".format(amenity1.__class__.__name__,
                                           amenity1.id)
            self.assertIn(stringAmenity, readFileAmenity)

    def test_save_Place(self):
        """
        Test to validate that you save the instance in
        the json file with the Place class
        """
        os.remove("file.json")
        place1 = Place()
        place1.save()
        with open("file.json", "r") as myFilePlace:
            readFilePlace = myFilePlace.read()
            stringPlace = "{}.{}".format(place1.__class__.__name__, place1.id)
            self.assertIn(stringPlace, readFilePlace)

    def test_save_Review(self):
        """
        Test to validate that you save the instance to
        the json file with the Review class
        """
        os.remove("file.json")
        review1 = Review()
        review1.save()
        with open("file.json", "r") as myFileReview:
            readFileReview = myFileReview.read()
            stringReview = "{}.{}".format(review1.__class__.__name__,
                                          review1.id)
            self.assertIn(stringReview, readFileReview)

    def test_reload(self):
        """
        Test to validate the reload
        """
        self.assertEqual(models.storage.reload(), None)
        models.storage.save()
        models.storage.reload()
        self.new = BaseModel()
        all_objs = models.storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        self.assertEqual(self.new.to_dict()['id'], obj.to_dict()['id'])
        self.assertTrue(os.path.exists('file.json'))
