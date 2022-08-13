#!/usr/bin/python3
"""review class module"""


from models.base_model import BaseModel


class Review(BaseModel):
    """review class details"""
    place_id = ""
    user_id = ""
    text = ""
