#!/usr/bin/python3
"""creating class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class with all attributes that are empty strings"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
