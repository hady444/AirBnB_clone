#!/usr/bin/python3
"""
unittests of basemodel
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test attributes
    """
    def setUp(self):
        pass
    def test_object_created(self):
        my_mod = BaseModel()
        my_mod.name = "first model"
        my_mod.my_number = 55
        self.assertEqual([my_mod.name, my_mod.my_number], ["first model", 55])
    def test_date_time
    if __name__ == '__main__':
        unittest.main()
