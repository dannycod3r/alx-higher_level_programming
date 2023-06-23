#!/usr/bin/python3
"""Module test for class Square"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """test class for square"""
    def setUp(self):
        """Reset the base __nb_object to zero before each test"""
        Square.__base__._Base__nb_objects = 0

    def test_initialization_of_square(self):
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (1) 1/3 - 3")
        self.assertEqual(Square(3, 1, 3).area(), 9)