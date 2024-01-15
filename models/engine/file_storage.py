#!/usr/bin/python3
"""FileStorage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_object = {}
        for key, value in self.__objects.items():
            serialized_object[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as my_file:
            json.dump(serialized_object, my_file)

    def reload(self):
        """Deserialization, convert json to instance if exists"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as my_file:
                loaded_objects = json.load(my_file)
#                self.__objects = {}
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_dict['__class__'] = class_name
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
