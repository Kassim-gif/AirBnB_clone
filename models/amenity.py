#!/usr/bin/python3
"""Defines tha Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): Tha name of tha amenity.
    """

    name = ""
