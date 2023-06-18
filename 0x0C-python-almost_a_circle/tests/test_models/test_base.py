#!/usr/bin/python3
"""Module to test for the class Base"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test cases for the class Base

    """
    # init test without id
    def test_initialization_without_id_increament_nb_objects(self):
        """Initialization without id must \
            increase the nb_object private attribue"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

        # init test with id
    def test_initialization_with_id_set_id_to_provided(self):
        """Set the id of object to the provided\
            one if set during initialisation"""
        self.assertEqual(Base(2).id, 2)
        self.assertEqual(Base(10).id, 10)
        self.assertEqual(Base(100).id, 100)
