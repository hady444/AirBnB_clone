#!/usr/bin/python3
"""
unittests of basemodel
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test attributes
    """
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_str_method(self):
        expected_output = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_output)

    def test_save_method(self):
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        my_model_json = self.my_model.to_dict()

        self.assertIn('__class__', my_model_json)
        self.assertEqual(my_model_json['__class__'], 'BaseModel')

        for key, value in self.my_model.__dict__.items():
            if isinstance(value, datetime):
                self.assertEqual(my_model_json[key], value.isoformat())
            else:
                self.assertEqual(my_model_json[key], value)

    def test_json_to_model(self):
        my_model_json = self.my_model.to_dict()
        new_model = BaseModel(**my_model_json)
        self.assertEqual(new_model.name, self.my_model.name)
        self.assertEqual(new_model.id, self.my_model.id)
        self.assertEqual(new_model.created_at, self.my_model.created_at)
        self.assertEqual(new_model.updated_at, self.my_model.updated_at)
        self.assertEqual(new_model.my_number, self.my_model.my_number)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)

    if __name__ == '__main__':
        unittest.main()
