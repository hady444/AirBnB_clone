#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import os
import models
import unittest
from models.state import State


class TestStateInstantiation(unittest.TestCase):
    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

class TestStateSave(unittest.TestCase):

    def test_save_updates_file(self):
        state = State()
        state.save()
        state_id = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(state_id, f.read())

class TestStateToDict(unittest.TestCase):

    def test_to_dict_output(self):
        state = State()
        state.id = "123456"
        state_dict = state.to_dict()
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': state.created_at.isoformat(),
            'updated_at': state.updated_at.isoformat(),
        }
        self.assertDictEqual(state_dict, tdict)

if __name__ == "__main__":
    unittest.main()
