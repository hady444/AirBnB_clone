#!/usr/bin/python3
"""test for Review"""
from models.review import Review
import unittest


class TestReviewModule(unittest.TestCase):
    """Test For Review"""
    def test_place_id_is_public_str(self):
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_public_str(self):
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_public_str(self):
        self.assertEqual(str, type(Review.text))

if __name__ == '__main__':
    unittest.main()
