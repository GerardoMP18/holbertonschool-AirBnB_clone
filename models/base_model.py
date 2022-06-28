#!/usr/bin/python3
"""
Creationg class Base Models
"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Creation of class BaseModel
    """
    def __init__(self):
        """
        Creation of constructor
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Function that represents the representation
        """
        string = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
        return string

    def save(self):
        """
        Function updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Function that returns a dictionary containing all the keys/values
        of __dict__ of the instance
        """
        format_d = '%Y-%m-%dT%H:%M:%S.%f'

        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.strftime(format_d)
        dictionary['updated_at'] = self.updated_at.strftime(format_d)
        return dictionary
