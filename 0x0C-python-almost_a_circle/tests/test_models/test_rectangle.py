#!/usr/bin/python3
"""Module test for class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test class for class Rectangle"""
    def test_initialization_rectangle_auto_set_id(self):
        """Test initialisation with and without id\
        should set respective attribute in the constructor"""
        self.assertEqual(Rectangle(2, 10).id, 1)  # no id, id = 1
        self.assertEqual(Rectangle(10, 2).id, 2)  # no id, id = 2
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)  # id = 12

    # tests for setters
    def test_width_set_correctly(self):
        """An instance can be created by setting the width"""
        pass

    def test_raise_exception_width_not_set(self):
        """Raise exception if width not set"""
        pass

    def test_height_set_correctly(self):
        """An instance can be created by setting height"""
        pass

    def test_raise_exception_height_not_set(self):
        """Raise exception if height not set"""
        pass

    def test_x_set_correctly(self):
        """An instance can be created by setting the x"""
        pass

    def test_raise_exception_x_not_set(self):
        """Raise exception if x not set"""
        pass

    def test_y_set_correctly(self):
        """An instance can be created by setting y"""
        pass

    def test_raise_exception_y_not_set(self):
        """Raise exception if y not set"""
        pass