#!/usr/bin/env python3
"""Review module containing class Review that inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """To create a new Review

    Args:
        BaseModel (BaseModel): super of class Review
    """
    def __init__(self, place_id="", user_id="", text="", **kwargs):
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
        super().__init__(**kwargs)
