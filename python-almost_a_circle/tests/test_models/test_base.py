#!/usr/bin/python3
"""Unittest module for Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up JSON files after tests."""
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_id_auto_increment(self):
        """Test auto incrementing id when id is None."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_explicit(self):
        """Test explicit id assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_explicit_and_auto(self):
        """Test mixture of explicit and auto-increment ids."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string with valid dictionaries list."""
        dicts = [{"id": 1, "x": 2, "y": 3}]
        json_str = Base.to_json_string(dicts)
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, '[{"id": 1, "x": 2, "y": 3}]')

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with valid JSON string."""
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        res = Base.from_json_string(json_str)
        self.assertEqual(res, [{"id": 89, "width": 10, "height": 4}])

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file with empty list."""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangle(self):
        """Test save_to_file with Rectangle instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            content = f.read()
        expected = Base.to_json_string([r1.to_dictionary(),
                                        r2.to_dictionary()])
        self.assertEqual(content, expected)

    def test_create_rectangle(self):
        """Test create method for Rectangle."""
        r1 = Rectangle(3, 5, 1, 2, 89)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """Test create method for Square."""
        s1 = Square(5, 1, 3, 99)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file does not exist."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        """Test load_from_file with Rectangle."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertEqual(len(output), 2)
        self.assertEqual(str(output[0]), str(r1))
        self.assertEqual(str(output[1]), str(r2))

    def test_load_from_file_square(self):
        """Test load_from_file with Square."""
        s1 = Square(5, 1, 3, 10)
        s2 = Square(7, 9, 1, 20)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertEqual(len(output), 2)
        self.assertEqual(str(output[0]), str(s1))
        self.assertEqual(str(output[1]), str(s2))


if __name__ == "__main__":
    unittest.main()
