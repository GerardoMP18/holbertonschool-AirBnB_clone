#!/usr/bin/python3
"""
FileStorage single instance creation
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
