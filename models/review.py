#!/usr/bin/python3
"""Defines tha Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): Tha Place id.
        user_id (str): Tha User id.
        text (str): Tha text of tha review.
    """

    place_id = ""
    user_id = ""
    text = ""
