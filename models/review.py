#!/usr/bin/python3
"""creating class review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """User class with all attributes that are empty strings"""
    place_id = ""
    user_id = ""
    text = ""
