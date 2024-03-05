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

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        return (self.__dict__)
