#!/usr/bin/python3
"""Module contains unittest for the function
max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaximumInteger(unittest.TestCase):
    """Test class for Maximum number test
    """

    # empty parameter
    def test_no_parameter_raise_exception(self):
        """Test if no parameter is passed"""
        self.assertRaises(TypeError, max_integer())

    # empty list
    def test_empty_list_return_none(self):
        """Test if list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_return_single_element_as_max(self):
        """Return the element if single in list"""
        m_list = [5]
        self.assertEqual(max_integer(m_list), 5)

    def test_return_max_given_list_of_sorted_positive_numbers(self):
        """Return max in numbers sorted"""
        m_list1 = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(m_list1), 5)

    def test_return_max_given_list_of_unsorted_positive_numbers(self):
        """Return max in numbers unsorted"""
        m_list2 = [6, 2, 9, 1, 0]
        self.assertEqual(max_integer(m_list2), 9)

    def test_return_max_given_list_of_equal_numbers(self):
        """Return max in equal numbers"""
        m_list3 = [2, 2, 2, 2, 2]
        self.assertEqual(max_integer(m_list3), 2)

# negatives
    def test_return_max_given_list_of_sorted_negative_numbers(self):
        """Return max in numbers sorted"""
        m_list11 = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(m_list11), -1)

    def test_return_max_given_list_of_unsorted_negative_numbers(self):
        """Return max in numbers unsorted"""
        m_list21 = [-6, -2, -9, -1, -3]
        self.assertEqual(max_integer(m_list21), -1)

    def test_return_max_given_list_of_equal_negative_numbers(self):
        """Return max in equal numbers"""
        m_list31 = [-2, -2, -2, -2, -2]
        self.assertEqual(max_integer(m_list31), -2)

    def test_return_max_from_mixed_numbers_of_integers(self):
        m_list41 = [0, -5, 6, -10, 50, 2, -4]
        self.assertEqual(max_integer(m_list41), 50)
