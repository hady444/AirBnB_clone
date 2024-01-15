#!/usr/bin/python3
"""test file_storage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Create an instance of FileStorage before each test
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up after each test
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_file_path_exists(self):
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))

    def test_objects_exists(self):
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))

    def test_all_method(self):
        self.assertEqual(self.storage.all(), {})

    def test_new_method(self):
        model = BaseModel()
        self.storage.new(model)
        self.assertIn('BaseModel.' + model.id, self.storage._FileStorage__objects)

    def test_save_method(self):
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            content = file.read()
            self.assertNotEqual(content, '')

    def test_reload_method(self):
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn('BaseModel.' + model.id, new_storage._FileStorage__objects)


class TestBaseModel(unittest.TestCase):
    def test_init_method(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_save_method(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)


if __name__ == '__main__':
    unittest.main()
