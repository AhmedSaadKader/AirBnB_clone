#!/usr/bin/env python3
"""City module containing class City that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """To create a new City

    Args:
        BaseModel (BaseModel): super of class City
    """
    def __init__(self, state_id="", name="", **kwargs):
        self.state_id = state_id
        self.name = name
        super().__init__(**kwargs)
