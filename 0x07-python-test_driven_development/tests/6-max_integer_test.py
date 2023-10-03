#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This class contains several test cases for the function max_integer"""

    def test_normal_list(self):
        """Test a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([98]), 98)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_max_at_beginning(self):
        """Test a list where the max is at the beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_max_at_middle(self):
        """Test a list where the max is at the middle"""
        self.assertEqual(max_integer([3, 2, 5, 4]), 5)

    def test_non_integers(self):
        """Test a list with non-integer elements"""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])

    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)


if __name__ == '__main__':
    unittest.main()
