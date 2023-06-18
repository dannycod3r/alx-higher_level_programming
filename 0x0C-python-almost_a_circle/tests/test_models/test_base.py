#!/usr/bin/python3
"""Module to test for the class Base"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):
    """Test cases for the class Base

    """
    # init test without id
    def test_initialization_without_an_id_increament_nb_objects(self):
        """Initialization without id must increase the nb_object private attribue"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)