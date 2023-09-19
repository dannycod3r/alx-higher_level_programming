#!/usr/bin/python3
"""Module contains tests for Rectangle class
"""

import unittest
from unittest.mock import patch
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle
    """

    def test_rectangle_inherits_base_class(self):
        """Test inheritance from Base model
        """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_attributes_in_rectangle_instance(self):
        """Test attributes of instance
        """
        r = Rectangle(2, 3)
        self.assertIn('id', dir(r))
        self.assertIn('_Rectangle__width', dir(r))
        self.assertIn('_Rectangle__height', dir(r))
        self.assertIn('_Rectangle__x', dir(r))
        self.assertIn('_Rectangle__x', dir(r))

    def test_object_is_instance_of_rectangle(self):
        """TEst is instance
        """
        r1 = Rectangle(5, 10)
        self.assertIsInstance(r1, Rectangle)

    def test_initialization_with_required_attributes(self):
        """Test init with required atributes
        """
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.width, 10)  # test getter
        self.assertEqual(r2.height, 2)

    def test_x_y_default_value_is_zero(self):
        """Test default values of x and y is zero
        """
        r4 = Rectangle(3, 5)
        self.assertEqual(r4.x, 0)
        self.assertEqual(r4.y, 0)

    def test_attribute_getters_return_correct_value(self):
        """Test getters
        """
        r3 = Rectangle(2, 5, 2, 3, 10)
        self.assertEqual(r3.id, 10)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 5)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r3.y, 3)

    # TypeError validation here
    ###########################
    def test_width_not_int_raises_type_error(self):
        """Test TypeError raised if width not int
        """
        # Use a lambda function to create the Rectangle
        #           instances within the context manager
        # This way, the TypeError will be caught by assertRaises
        self.assertRaises(TypeError, lambda: Rectangle("2", 10))
        self.assertRaises(TypeError, lambda: Rectangle(2.5, 10))
        self.assertRaises(TypeError, lambda: Rectangle(None, 10))
        self.assertRaises(TypeError, lambda: Rectangle([5], 10))
        self.assertRaises(TypeError, lambda: Rectangle((5,), 10))
        self.assertRaises(TypeError, lambda: Rectangle(float("nan"), 10))
        self.assertRaises(TypeError, lambda: Rectangle(True, 10))

    def test_height_not_int_raises_type_error(self):
        """Test TypeError raised if height not int
        """
        # Use a lambda function to create the Rectangle
        #           instances within the context manager
        # This way, the TypeError will be caught by assertRaises
        self.assertRaises(TypeError, lambda: Rectangle(10, "2"))
        self.assertRaises(TypeError, lambda: Rectangle(10, 2.5))
        self.assertRaises(TypeError, lambda: Rectangle(5, None))
        self.assertRaises(TypeError, lambda: Rectangle(10, [5]))
        self.assertRaises(TypeError, lambda: Rectangle(10, (5,)))
        self.assertRaises(TypeError, lambda: Rectangle(10, float("nan")))
        self.assertRaises(TypeError, lambda: Rectangle(10, True))

    def test_x_not_int_raises_type_error(self):
        """Test TypeError raised if x not int
        """
        # Use a lambda function to create the Rectangle
        #           instances within the context manager
        # This way, the TypeError will be caught by assertRaises
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, "2", 8))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, 2.5, 8))
        self.assertRaises(TypeError, lambda: Rectangle(5, 4, None, 8))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, [5], 8))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, (5,), 8))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, float("nan"), 8))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, True, 8))

    def test_y_not_int_raises_type_error(self):
        """Test TypeError raised if y not int
        """
        # Use a lambda function to create the Rectangle
        #           instances within the context manager
        # This way, the TypeError will be caught by assertRaises
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, 8, "2"))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, 8, 2.5))
        self.assertRaises(TypeError, lambda: Rectangle(5, 4, 8, None))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, 8, [5]))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, 8, (5,)))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, 8, float("nan")))
        self.assertRaises(TypeError, lambda: Rectangle(10, 4, 8, True))

    # ValueError validation here
    ############################
    def test_width_under_or_equals_zero_raises_value_error(self):
        """Test ValueError
        """
        self.assertRaises(ValueError, lambda: Rectangle(0, 10))
        self.assertRaises(ValueError, lambda: Rectangle(-10, 10))

    def test_height_under_or_equals_zero_raises_value_error(self):
        """Test ValueError
        """
        self.assertRaises(ValueError, lambda: Rectangle(10, 0))
        self.assertRaises(ValueError, lambda: Rectangle(10, -10))

    def test_x_under_zero_raises_value_error(self):
        """TEst ValueError
        """
        self.assertRaises(ValueError, lambda: Rectangle(10, 10, -5, 10))

    def test_y_under_zero_raises_value_error(self):
        """Test ValueError
        """
        self.assertRaises(ValueError, lambda: Rectangle(10, 10, 5, -10))

    # TODO: Test initialization with number of args

    # Test Area Here
    def test_area_return_product_of_width_and_height(self):
        """TEst Area
        """
        r5 = Rectangle(4, 5)
        self.assertAlmostEqual(r5.area(), 20)

    # Test display with symbol
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_rectangle_with_symbol(self, mock_stdout):
        """TEst display method
        """
        # rectangle instance
        r6 = Rectangle(4, 3)

        # Call the display method, which will print to mock_stdout
        r6.display()

        # Get the captured output
        displayed_output = mock_stdout.getvalue()

        expected_output = '####\n####\n####\n\n'

        self.assertEqual(expected_output, displayed_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_rectangle_handle_x_y(self, mock_stdout):
        """Test display handle x and y
        """
        # rectangle instance
        r7 = Rectangle(4, 3, 2, 2)

        # call display method
        r7.display()

        # catch the displayed output
        displayed_output = mock_stdout.getvalue()

        expected_output = '\n\n  ####\n  ####\n  ####\n\n'

        self.assertEqual(expected_output, displayed_output)

    def test_str_returns_custom_output(self):
        """Test string
        """
        r8 = Rectangle(4, 6, 2, 1, 12)

        self.assertEqual(str(r8), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_should_replace_attributes_with_argument(self):
        """Test update method
        """
        pass
        r9 = Rectangle(10, 10, 10, 10, 20)
        self.assertEqual(str(r9), "[Rectangle] (20) 10/10 - 10/10")

        r9.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r9), "[Rectangle] (89) 4/5 - 2/3")

    # TODO:
    # test args and kwargs
