#!/usr/bin/python3
"""Defines tha User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        email (str): Tha email of tha user.
        password (str): Tha password of tha user.
        first_name (str): Tha first name of tha user.
        last_name (str): Tha last name of tha user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
