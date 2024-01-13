#!/usr/bin/python3
"""Base Module"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        return ("[{}], ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        dic = dict()
        dic['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dic[key] = value.isoformat()
                continue
            dic[key] = value
        return dic
