#!/usr/bin/python3
"""DEfining gthe class BaseModel"""
import json
import uuid
from datetime import datetime

class BaseModel:
    """Representing the base model"""

    def __init__(self):
        """Initializing a new Rectangle"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now
        self.updated_at = datetime.now
    def __str__(self):
        """Returns the string rep. of the base class"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        """updates the instance attribute updated_at with cuurent time"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """Returns the dictionary representation of a Baseclass"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__ ': self.__class__
        }
if __name__ == "__main__":
    base_model = BaseModel()
    print(base_model)
