#!/usr/bin/env python3
"""This module contains the base model used for all other models
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base model for all other models
    """

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = self._parse_value('created_at', kwargs.get('created_at'))
        self.updated_at = self._parse_value('updated_at', kwargs.get('updated_at'))
        for key, value in kwargs.items():
            if key not in ['id', 'created_at', 'updated_at']:
                if key != '__class__':
                    setattr(self, key, value)

    def _parse_value(self, method, value):
        """parse the values of the kwargs dictionary of init
        """
        if not value:
            value = datetime.now()
        elif isinstance(value, str):
            value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        elif not isinstance(value, datetime):
            raise ValueError(f"{method} must be a datetime object")
        return value

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save instance to file
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""
        my_dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
