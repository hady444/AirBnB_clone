#!/usr/bin/python3
"""test for User"""
from models.user import User
import unittest

class TestUserModule(unittest.TestCase):
    """Test For user """
    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

if __name__ == '__main__':
    unittest.main()
