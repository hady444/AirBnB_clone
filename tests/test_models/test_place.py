#!/usr/bin/python3
"""test for Place"""
from models.place import Place
import unittest


class TestPlaceModule(unittest.TestCase):
    """Test For Place"""
    def test_city_id_is_public_str(self):
        self.assertEqual(str, type(Place.city_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Place.user_id))

    # Add other tests for remaining attributes

if __name__ == '__main__':
    unittest.main()
