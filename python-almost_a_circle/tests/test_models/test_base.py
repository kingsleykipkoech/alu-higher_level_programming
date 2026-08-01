#!/usr/bin/python3
"""Unittest module for Base class."""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Tests for Base class instantiation."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_no_arg(self):
        """Test Base with no argument."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """Test auto incrementing id."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_none_id(self):
        """Test None id."""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_unique_id(self):
        """Test explicit id assignment."""
        self.assertEqual(89, Base(89).id)

    def test_nb_instances_after_unique_id(self):
        """Test auto-increment after explicit id."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_id_public(self):
        """Test id is public and can be modified."""
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """Test __nb_objects is private."""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_objects)

    def test_zero_id(self):
        """Test id of zero."""
        self.assertEqual(0, Base(0).id)

    def test_negative_id(self):
        """Test negative id."""
        self.assertEqual(-1, Base(-1).id)

    def test_str_id(self):
        """Test string id."""
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        """Test float id."""
        self.assertEqual(5.5, Base(5.5).id)

    def test_list_id(self):
        """Test list id."""
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict_id(self):
        """Test dict id."""
        self.assertEqual({"a": 1}, Base({"a": 1}).id)

    def test_tuple_id(self):
        """Test tuple id."""
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_bool_id(self):
        """Test bool id."""
        self.assertEqual(True, Base(True).id)

    def test_inf_id(self):
        """Test infinity id."""
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_nan_id(self):
        """Test NaN id."""
        b = Base(float('nan'))
        self.assertNotEqual(b.id, b.id)

    def test_two_args(self):
        """Test Base with two arguments."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Tests for Base.to_json_string()."""

    def test_to_json_string_rectangle_type(self):
        """Test to_json_string returns string."""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        """Test to_json_string with one Rectangle dict."""
        r = Rectangle(10, 7, 2, 8, 6)
        result = Base.to_json_string([r.to_dictionary()])
        self.assertTrue(len(result) > 0)

    def test_to_json_string_rectangle_two_dicts(self):
        """Test to_json_string with two Rectangle dicts."""
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        result = Base.to_json_string(list_dicts)
        self.assertIsInstance(result, str)

    def test_to_json_string_square_type(self):
        """Test to_json_string returns string for Square."""
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        """Test to_json_string with one Square dict."""
        s = Square(10, 2, 3, 4)
        result = Base.to_json_string([s.to_dictionary()])
        self.assertTrue(len(result) > 0)

    def test_to_json_string_empty_list(self):
        """Test to_json_string with empty list."""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        """Test to_json_string with no args."""
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestBaseFromJsonString(unittest.TestCase):
    """Tests for Base.from_json_string()."""

    def test_from_json_string_type(self):
        """Test from_json_string returns list."""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        """Test from_json_string with one Rectangle."""
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        """Test from_json_string with two Rectangles."""
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        """Test from_json_string with one Square."""
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        """Test from_json_string with empty string."""
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_no_args(self):
        """Test from_json_string with no args."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file()."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up JSON files after tests."""
        for fn in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(fn):
                os.remove(fn)

    def test_save_to_file_one_rectangle(self):
        """Test save_to_file with one Rectangle."""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_save_to_file_two_rectangles(self):
        """Test save_to_file with two Rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 0, 0, 6)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 2)

    def test_save_to_file_one_square(self):
        """Test save_to_file with one Square."""
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)

    def test_save_to_file_two_squares(self):
        """Test save_to_file with two Squares."""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 2)

    def test_save_to_file_cls_name_for_filename(self):
        """Test that filename matches class name."""
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        self.assertTrue(os.path.exists("Square.json"))

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_no_args(self):
        """Test save_to_file with no args."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_overwrite(self):
        """Test that save_to_file overwrites existing file."""
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            content = json.loads(f.read())
        self.assertEqual(len(content), 1)


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create()."""

    def test_create_rectangle_original(self):
        """Test create with Rectangle."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        """Test create returns new instance."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        """Test created instance is not equal."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        """Test create with Square."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        """Test create returns new instance."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        """Test created instance is not equal."""
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file()."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up JSON files after tests."""
        for fn in ["Rectangle.json", "Square.json"]:
            if os.path.exists(fn):
                os.remove(fn)

    def test_load_from_file_first_rectangle(self):
        """Test load_from_file with Rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(output[0]))

    def test_load_from_file_second_rectangle(self):
        """Test load_from_file second Rectangle."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(output[1]))

    def test_load_from_file_rectangle_types(self):
        """Test load_from_file returns list of Rectangles."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertIsInstance(output[0], Rectangle)

    def test_load_from_file_first_square(self):
        """Test load_from_file with Squares."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertEqual(str(s1), str(output[0]))

    def test_load_from_file_second_square(self):
        """Test load_from_file second Square."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertEqual(str(s2), str(output[1]))

    def test_load_from_file_square_types(self):
        """Test load_from_file returns list of Squares."""
        s1 = Square(5, 1, 3, 3)
        Square.save_to_file([s1])
        output = Square.load_from_file()
        self.assertIsInstance(output[0], Square)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file does not exist."""
        output = Rectangle.load_from_file()
        self.assertEqual([], output)


if __name__ == "__main__":
    unittest.main()
