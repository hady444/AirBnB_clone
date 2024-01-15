#!/usr/bin/python3
"""test for City"""
from models.city import City
import unittest


class TestCityModule(unittest.TestCase):
    """Test For City"""
    def test_state_id_is_public_str(self):
        self.assertEqual(str, type(City.state_id))

    def test_name_is_public_str(self):
        self.assertEqual(str, type(City.name))

if __name__ == '__main__':
    unittest.main()
