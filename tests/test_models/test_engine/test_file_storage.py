#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        # Ensure the test file does not exist initially
        self.file_path = "test_file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        # Create a new FileStorage instance
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        # Remove the test file after each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        my_model = BaseModel()
        self.storage.new(my_model)
        all_objects = self.storage.all()
        self.assertIn(my_model, all_objects.values())

    def test_save_and_reload_methods(self):
        my_model = BaseModel()
        my_model.name = "Test_Model"
        self.storage.new(my_model)
        self.storage.save()

        # Create a new FileStorage instance to simulate a program restart
        new_storage = FileStorage()
        new_storage.reload()

        # Check if the reloaded storage contains the saved object
        reloaded_objects = new_storage.all()
        self.assertTrue(any(obj.__dict__ == my_model.__dict__ for obj in reloaded_objects.values()))

    def test_save_method_creates_file(self):
        # Check if calling save method creates a file
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

#    def test_reload_method_ignores_nonexistent_file(self):
        # Check if calling reload method with a nonexistent file does not raise an error
#        non_existent_file_path = "non_existent_file.json"
#        self.storage._FileStorage__file_path = non_existent_file_path
#        self.storage.reload()  # Should not raise an error

if __name__ == '__main__':
    unittest.main()
