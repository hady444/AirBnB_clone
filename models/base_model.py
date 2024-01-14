#!/usr/bin/python3
"""Base Module"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    pard = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, pard)
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        dic = dict()
        dic['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dic[key] = value.isoformat()
                continue
            dic[key] = value
        return dic
