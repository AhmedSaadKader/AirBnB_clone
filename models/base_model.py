#!/usr/bin/env python3
"""This module contains the base model used for all other models
"""


class BaseModel:
    """Base model for all other models
    """
    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def save(self):
        """save instance
        """

    def to_json(self):
        """convert to json
        """
