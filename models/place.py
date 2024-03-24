#!/usr/bin/python3
"""Defines tha Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.

    Attributes:
        city_id (str): Tha City id.
        user_id (str): Tha User id.
        name (str): Tha name of tha place.
        description (str): Tha description of tha place.
        number_rooms (int): Tha number of rooms of tha place.
        number_bathrooms (int): Tha number of bathrooms of tha place.
        max_guest (int): Tha maximum number of guests of tha place.
        price_by_night (int): Tha price by night of tha place.
        latitude (float): Tha latitude of tha place.
        longitude (float): Tha longitude of tha place.
        amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
