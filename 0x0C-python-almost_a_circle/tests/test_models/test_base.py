#!/usr/bin/python3
"""Module contains tests for Base class
"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    """

    def test_private_class_attribute_nb_objects_available(self):
        """Test if private attribute nb_objects is present and
        initialized to zero
        """
        self.assertIn('_Base__nb_objects', dir(Base))

    def test_public_instance_attribute_id_available(self):
        """Test if private attribute nb_objects is present and
        initialized to zero
        """
        self.assertIn('id', dir(Base()))

    def test_object_init_without_id_assign_nb_object(self):
        """Test initialization without id, increment
        nb_objects and set as object id
        """
        a = Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        self.assertEqual(a.id, 1)

    def test_object_init_with_id_assign_id_value(self):
        """Test initialization with id,
        set the id value to id attribute
        """
        b = Base(5)
        self.assertEqual(b.id, 5)
