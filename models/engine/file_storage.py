#!/usr/bin/python3
"""FileStorage module"""
import json

class FileStorage:
    """
    FileStorage class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = obj.id

    def save(self):
        serialized_object = {}
        for key, value in self.__dict__:
            serialized_object[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='usf-8') as my_file:
            json.dump(serialized_object, my_file)

    def reload(self):
        try:
            with open(self.__file_path, '', encoding='usf-8') as my_file:
            self.__objects = json.load(my_file)
            for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_dict['__class__'] = class_name
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
