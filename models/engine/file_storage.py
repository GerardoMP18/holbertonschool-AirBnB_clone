#!/usr/bin/python3
"""
Store first object
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Creation of storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Function to return the dictionary of __objects
        """
        dictionary = self.__objects
        return dictionary

    def new(self, obj):
        """
        Funcion sets in __objects the obj with key <obj class name>.id
        """
        string = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[string] = obj

    def save(self):
        """
        Function that saves and serializes them into __objects in the json file
        """
        my_dict = {}
        with open(self.__file_path, mode="w", encoding="utf-8") as myFile:
            all_dictionary = self.__objects
            for keys, values in all_dictionary.items():
                my_dict[keys] = values.to_dict()
            json.dump(my_dict, myFile)

    def reload(self):
        """
        Function that deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as myFile:
                deserializa = json.load(myFile)
                for keys, values in deserializa.items():
                    name_class = eval(values["__class__"])
                    self.__objects[keys] = name_class(**values)
