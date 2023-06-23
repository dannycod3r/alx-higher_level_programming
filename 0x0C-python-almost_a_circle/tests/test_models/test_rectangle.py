#!/usr/bin/python3
"""Module test for class Rectangle"""
import unittest
from unittest.mock import patch
from io import StringIO
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
        self.assertEqual(Rectangle(2, 100, 0, 0, 12).height, 100)  # h = 100

    def test_raise_exception_height_not_set(self):
        """Raise exception if height not set"""
        with self.assertRaises(ValueError):
            Rectangle(2, -10)
            Rectangle(1, -1000)
            Rectangle(10, 0)

        with self.assertRaises(TypeError):
            Rectangle(10, "2")
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

    # test for area of rectangle
    def test_return_area_of_rectangle(self):
        """An instance should return the area"""
        self.assertEqual(Rectangle(3, 2).area(), 6)  # 3*2
        self.assertEqual(Rectangle(3, 3).area(), 9)
        self.assertEqual(Rectangle(2, 10).area(), 20)  # 2*10
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)  # 8*7

    # test printing to stdout
    # https://ryip.me/posts/python/unittest-stdout-stderr/
    ######################################################
    def test_display_rectangle_with_sign(self):
        """Test printing of rectangle with sign"""
        # test for 4, 6
        output = StringIO()

        with patch("sys.stdout", new=output):
            Rectangle(4, 6).display()

        extected_out = '####\n####\n####\n####\n####\n####\n'

        displayed_output = output.getvalue()
        self.assertEqual(displayed_output, extected_out)

        # test for 2, 2
        output = StringIO()

        with patch("sys.stdout", new=output):
            Rectangle(2, 2).display()

        extected_out = '##\n##\n'

        displayed_output = output.getvalue()
        self.assertEqual(displayed_output, extected_out)

    # test for __str__
    def test_str_representation(self):
        """Test __str__ for correct display"""
        self.assertEqual(
            str(Rectangle(4, 6, 2, 1, 12)), "[Rectangle] (12) 2/1 - 4/6"
            )

    # test display with x, y
    def test_display_x_and_y(self):
        """Test rectangle dislay with x, y displacement"""
        # test for 4, 6
        output = StringIO()

        with patch("sys.stdout", new=output):
            Rectangle(2, 3, 2, 2).display()

        extected_out = '\n\n  ##\n  ##\n  ##\n'

        displayed_output = output.getvalue()
        self.assertEqual(displayed_output, extected_out)

    def test_update_rectangle_details(self):
        """Successfully update the rectangle details"""
        self.rect = Rectangle(10, 10, 10, 10)
        self.rect.update(89)
        self.assertEqual(str(self.rect), "[Rectangle] (89) 10/10 - 10/10")

        self.rect.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.rect), "[Rectangle] (89) 4/5 - 2/3")
