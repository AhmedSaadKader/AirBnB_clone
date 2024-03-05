#!/usr/bin/env python3
"""Module containing FileStorage class that moderates instances and
json
"""
import json


class FileStorage():
    """Serializes instances to JSON file and deserializes JSON file to
    instances
    """
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        Args:
            obj (BaseModel): BaseModel object
        """
        self.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __file_path)
        """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """read storage file, parse the JSON string and re-create
        Student objects
        """
        with open(self.__file_path, encoding="utf-8") as f:
            return json.loads(f.read())
