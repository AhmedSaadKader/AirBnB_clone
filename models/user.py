#!/usr/bin/env python3
"""user module containing class User that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """To create a new user

    Args:
        BaseModel (BaseModel): super of class User
    """
    # def __init__(self, email="", password="",
    #              first_name="", last_name="", **kwargs):
    #     self.email = email
    #     self.password = password
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     super().__init__(**kwargs)

    email = ""
    password = ""
    first_name = ""
    last_name = ""
