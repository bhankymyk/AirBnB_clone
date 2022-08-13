#!usr/bin/python3
"""class BaseModel"""

import uuid
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes and methods
    for other classes
    """

    def __init__(self, *args, **kwargs):
        """method to instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.striptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    continue

                setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(Self)

    def save(self):
        """Save new information"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary representation of the instances
        containing keys/values"""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
                dict_repr["__class__"] = type(self).__name__
                return dict_repr

    def __str__(self):
        """print the name of the dictionary"""
        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)
