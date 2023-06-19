#!/usr/bin/python3
"""Module test for class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test class for class Rectangle"""
    def test_initialization_rectangle_auto_set_id(self):
        """Test initialisation with and without id\
        should set respective attribute in the constructor"""
        self.assertEqual(Rectangle(2, 10).id, 1) # no id, id = 1
        self.assertEqual(Rectangle(10, 2).id, 2) # no id, id = 2
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12) # id = 12
