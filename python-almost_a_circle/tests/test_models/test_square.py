#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Test Square inherits from Rectangle and Base."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_instantiation(self):
        """Test Square instantiation."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(5, 2, 3, 12)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 12)

    def test_size_getter_setter(self):
        """Test size getter and setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_validation(self):
        """Test exception handling for size setter."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "10"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -5
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

    def test_area(self):
        """Test inherited area method for Square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test __str__ output for Square."""
        s = Square(5, 1, 2, 10)
        self.assertEqual(str(s), "[Square] (10) 1/2 - 5")

    def test_display(self):
        """Test display method for Square."""
        s = Square(2, 1, 1)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_update_args(self):
        """Test update method with *args for Square."""
        s = Square(5, 0, 0, 1)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(1, 2)
        self.assertEqual(s.size, 2)
        s.update(1, 2, 3)
        self.assertEqual(s.x, 3)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update method with **kwargs for Square."""
        s = Square(5, 0, 0, 1)
        s.update(x=12)
        self.assertEqual(s.x, 12)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)
        s.update(size=7, id=89, y=1)
        self.assertEqual(s.id, 89)

    def test_to_dictionary(self):
        """Test to_dictionary method for Square."""
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        expected = {"id": 1, "size": 10, "x": 2, "y": 1}
        self.assertEqual(s_dict, expected)


if __name__ == "__main__":
    unittest.main()
