#!/usr/bin/env python3
"""Amenity module containing class Amenity that inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """To create a new Amenity

    Args:
        BaseModel (BaseModel): super of class Amenity
    """
    def __init__(
            self, email="", password="", first_name="", last_name="", **kwargs
            ):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        super().__init__(**kwargs)
