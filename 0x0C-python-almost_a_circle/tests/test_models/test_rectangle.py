#!/usr/bin/python3
"""Module test for class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test class for class Rectangle"""
    def setUp(self):
        """Reset the base __nb_object to zero before each test"""
        Rectangle.__base__._Base__nb_objects = 0

    def test_initialization_rectangle_auto_set_id(self):
        """Test initialisation with and without id\
        should set respective attribute in the constructor"""
        self.assertEqual(Rectangle(2, 10).id, 1)  # no id, id = 1
        self.assertEqual(Rectangle(10, 2).id, 2)  # no id, id = 2
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)  # id = 12

    # tests for setters
    # width
    def test_width_set_correctly(self):
        """An instance can be created by setting the width"""
        self.assertEqual(Rectangle(2, 10).width, 2)  # width = 2
        self.assertEqual(Rectangle(10, 2).width, 10)  # width = 10
        self.assertEqual(Rectangle(100, 2, 0, 0, 12).width, 100)  # width = 100

    def test_raise_exception_width_not_set(self):
        """Raise exception if width not set"""
        with self.assertRaises(ValueError):
            Rectangle(-2, 10)
            Rectangle(-1000, 1)
            Rectangle(0, 10)

        with self.assertRaises(TypeError):
            Rectangle("2", 10)
            Rectangle(2.5, 10)
            Rectangle(None, 10)

    # height
    def test_height_set_correctly(self):
        """An instance can be created by setting height"""
        self.assertEqual(Rectangle(2, 10).height, 10)  # height = 10
        self.assertEqual(Rectangle(10, 2).height, 2)  # height = 2
        self.assertEqual(Rectangle(2, 100, 0, 0, 12).height, 100)  # height = 100

    def test_raise_exception_height_not_set(self):
        """Raise exception if height not set"""
        with self.assertRaises(ValueError):
            Rectangle(2, -10)
            Rectangle(1, -1000)
            Rectangle(10, 0)

        with self.assertRaises(TypeError):
            Rectangle(10,"2")
            Rectangle(25, 2.3)
            Rectangle(10, None)

    # test for x
    def test_x_set_correctly(self):
        """An instance can be created by setting the x"""
        self.assertEqual(Rectangle(10, 2).x, 0)  # 0 if not set
        self.assertEqual(Rectangle(10, 2, 3, 1).x, 3)  # x = 3
        self.assertEqual(Rectangle(10, 2, 0, 1).x, 0)  # x = 0
        self.assertEqual(Rectangle(10, 2, 1000, 1).x, 1000)

    def test_raise_exception_x_not_set(self):
        """Raise exception if x not set"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -3, 1)
            Rectangle(10, 2, 3.5, 1)

        with self.assertRaises(TypeError):
            Rectangle(10, 2, "2", 1)
            Rectangle(10, 3.5, None, 5)

    # test for y
    def test_y_set_correctly(self):
        """An instance can be created by setting y"""
        self.assertEqual(Rectangle(10, 2).y, 0)  # 0 if not set
        self.assertEqual(Rectangle(10, 2, 3, 1).y, 1)  # x = 1
        self.assertEqual(Rectangle(10, 2, 0, 0).y, 0)  # x = 0
        self.assertEqual(Rectangle(10, 2, 10, 1000).y, 1000)  # x = 1000

    def test_raise_exception_y_not_set(self):
        """Raise exception if y not set"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)
            Rectangle(10, 2, 5, 15.3)

        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "2")
            Rectangle(10, 3.5, 5, None)
