#!/usr/bin/python3
"""Defines tha City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): Tha state id.
        name (str): Tha name of tha city.
    """

    state_id = ""
    name = ""
