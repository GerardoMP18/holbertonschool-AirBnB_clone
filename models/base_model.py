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
    format_date = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Creation of constructor and
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, self.format_date)
                    setattr(self, key, value)
        else:
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
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.strftime(self.format_date)
        dictionary['updated_at'] = self.updated_at.strftime(self.format_date)
        return dictionary
