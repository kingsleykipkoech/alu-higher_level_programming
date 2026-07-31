#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list with max value at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([1.53, 6.33, -1.2, 4.2]), 6.33)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        self.assertEqual(max_integer([1.53, 14.5, 9, -6]), 14.5)

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer("Brennan"), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["Brennan", "is", "the", "best"]), "the")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_negative_numbers(self):
        """Test a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)


if __name__ == "__main__":
    unittest.main()
