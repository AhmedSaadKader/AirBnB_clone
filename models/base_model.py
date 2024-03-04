#!/usr/bin/env python3
"""This module contains the base model used for all other models
"""
import json

class BaseModel:
    """Base model for all other models
    """
    filename = "/engine/file_storage.py"
    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self, filename):
        """save instance to file
        """
        my_instance = self.to_json()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(my_instance)

    def to_json(self):
        """convert to json
        """
        return json.dumps(self)

    def reload(self):
        """read storage file, parse the JSON string and re-create
        Student objects
        """
