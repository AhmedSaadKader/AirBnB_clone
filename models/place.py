#!/usr/bin/env python3
"""Place module containing class Place that inherits from BaseModel
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """To create a new Place

    Args:
        BaseModel (BaseModel): super of class Place
    """
    def __init__(self, city_id="", user_id="", name="", description="",
                number_rooms=0, number_bathrooms=0, max_guest=0,
                price_by_night=0, latitude=0.0, longititude=0.0,
                amenity_ids=[], **kwargs):
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longititude
        self.amenity_ids = amenity_ids
        super().__init__(**kwargs)