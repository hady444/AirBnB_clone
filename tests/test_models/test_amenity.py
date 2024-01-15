#!/usr/bin/python3
"""test for Amenity"""
from models.amenity import Amenity
import unittest


class TestAmenityModule(unittest.TestCase):
    """Test For Amenity"""
    def test_name_is_public_str(self):
        self.assertEqual(str, type(Amenity.name))

if __name__ == '__main__':
    unittest.main()
