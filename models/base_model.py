#!/usr/bin/env python3
"""This module contains the base model used for all other models
"""
import json
import uuid
import datetime


class BaseModel:
    """Base model for all other models
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """save instance to file
        """
        # my_instance = json.dumps(self)
        # with open(filename, "w", encoding="utf-8") as f:
        #     f.write(my_instance)

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        return (self.__dict__)

    def to_json(self):
        """convert to json
        """
        return json.dumps(self)

