#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User

class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

class TestUserSave(unittest.TestCase):
    """Unittests for testing save method of the User class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        us = User()
        sleep(0.05)
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

class TestUserToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

if __name__ == "__main__":
    unittest.main()

