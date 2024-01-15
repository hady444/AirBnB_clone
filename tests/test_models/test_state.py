#!/usr/bin/python3
"""test for State"""
from models.state import State
import unittest


class TestStateModule(unittest.TestCase):
    """Test For State"""
    def test_name_is_public_str(self):
        self.assertEqual(str, type(State.name))

if __name__ == '__main__':
    unittest.main()
