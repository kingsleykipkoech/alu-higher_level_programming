#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Tests for Square class instantiation."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_square_is_base(self):
        """Test Square inherits from Base."""
        self.assertIsInstance(Square(10), Base)

    def test_square_is_rectangle(self):
        """Test Square inherits from Rectangle."""
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_args(self):
        """Test Square with no arguments."""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """Test Square with one argument."""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """Test Square with two arguments."""
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        """Test Square with three arguments."""
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """Test Square with four arguments."""
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        """Test Square with more than four arguments."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        """Test size is not a private attribute directly."""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """Test size getter."""
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        """Test size setter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        """Test width getter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        """Test height getter."""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)


class TestSquareSize(unittest.TestCase):
    """Tests for Square size validation."""

    def test_none_size(self):
        """Test None size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        """Test string size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        """Test float size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_list_size(self):
        """Test list size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_dict_size(self):
        """Test dict size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2})

    def test_bool_size(self):
        """Test bool size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_tuple_size(self):
        """Test tuple size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1,))

    def test_set_size(self):
        """Test set size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2})

    def test_negative_size(self):
        """Test negative size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        """Test zero size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquareX(unittest.TestCase):
    """Tests for Square x validation."""

    def test_none_x(self):
        """Test None x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        """Test string x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x(self):
        """Test float x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_list_x(self):
        """Test list x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_dict_x(self):
        """Test dict x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2})

    def test_bool_x(self):
        """Test bool x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_negative_x(self):
        """Test negative x."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquareY(unittest.TestCase):
    """Tests for Square y validation."""

    def test_none_y(self):
        """Test None y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_str_y(self):
        """Test string y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_float_y(self):
        """Test float y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_list_y(self):
        """Test list y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_dict_y(self):
        """Test dict y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_bool_y(self):
        """Test bool y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, True)

    def test_negative_y(self):
        """Test negative y."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquareArea(unittest.TestCase):
    """Tests for Square area method."""

    def test_area_small(self):
        """Test area with small values."""
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_area_large(self):
        """Test area with large values."""
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes(self):
        """Test area after changing attributes."""
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_area_one_arg(self):
        """Test area with one arg."""
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquareDisplay(unittest.TestCase):
    """Tests for Square display method."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    @staticmethod
    def capture_stdout(sq):
        """Capture and return stdout output from display()."""
        captured = io.StringIO()
        sys.stdout = captured
        sq.display()
        sys.stdout = sys.__stdout__
        return captured

    def test_display_size(self):
        """Test display with size only."""
        s = Square(2, 0, 0, 9)
        capture = TestSquareDisplay.capture_stdout(s)
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_size_x(self):
        """Test display with x offset."""
        s = Square(3, 1, 0, 18)
        capture = TestSquareDisplay.capture_stdout(s)
        self.assertEqual(" ###\n ###\n ###\n", capture.getvalue())

    def test_display_size_y(self):
        """Test display with y offset."""
        s = Square(4, 0, 1, 9)
        capture = TestSquareDisplay.capture_stdout(s)
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_size_x_y(self):
        """Test display with x and y offsets."""
        s = Square(2, 3, 2, 1)
        capture = TestSquareDisplay.capture_stdout(s)
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        """Test display with one arg."""
        s = Square(5, 1, 2, 4)
        with self.assertRaises(TypeError):
            s.display(1)


class TestSquareStr(unittest.TestCase):
    """Tests for Square __str__ method."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_str_method_print_size(self):
        """Test __str__ with size."""
        s = Square(4)
        correct = "[Square] (1) 0/0 - 4"
        self.assertEqual(correct, str(s))

    def test_str_method_size_x(self):
        """Test __str__ with size and x."""
        s = Square(5, 5)
        correct = "[Square] (1) 5/0 - 5"
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y(self):
        """Test __str__ with size, x, and y."""
        s = Square(7, 4, 22)
        correct = "[Square] (1) 4/22 - 7"
        self.assertEqual(correct, str(s))

    def test_str_method_size_x_y_id(self):
        """Test __str__ with all arguments."""
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changed_attributes(self):
        """Test __str__ after changing attributes."""
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(s))

    def test_str_method_one_arg(self):
        """Test __str__ with one arg."""
        s = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s.__str__(1)


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for Square update method with *args."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_update_args_zero(self):
        """Test update with no args."""
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))

    def test_update_args_one(self):
        """Test update with one arg (id)."""
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual("[Square] (89) 10/10 - 10", str(s))

    def test_update_args_two(self):
        """Test update with two args (id, size)."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_args_three(self):
        """Test update with three args."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3)
        self.assertEqual("[Square] (89) 3/10 - 2", str(s))

    def test_update_args_four(self):
        """Test update with four args."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_more_than_four(self):
        """Test update with more than four args."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_args_width_setter(self):
        """Test width updates properly through *args."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.width)

    def test_update_args_height_setter(self):
        """Test height updates properly through *args."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2)
        self.assertEqual(2, s.height)


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for Square update method with **kwargs."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_update_kwargs_one(self):
        """Test update with one kwarg."""
        s = Square(10, 10, 10, 10)
        s.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(s))

    def test_update_kwargs_two(self):
        """Test update with two kwargs."""
        s = Square(10, 10, 10, 10)
        s.update(size=2, id=1)
        self.assertEqual("[Square] (1) 10/10 - 2", str(s))

    def test_update_kwargs_three(self):
        """Test update with three kwargs."""
        s = Square(10, 10, 10, 10)
        s.update(size=2, y=3, id=89)
        self.assertEqual("[Square] (89) 10/3 - 2", str(s))

    def test_update_kwargs_four(self):
        """Test update with four kwargs."""
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(s))

    def test_update_args_and_kwargs(self):
        """Test update with both args and kwargs, args take precedence."""
        s = Square(10, 10, 10, 10)
        s.update(89, 2, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(s))

    def test_update_kwargs_wrong_keys(self):
        """Test update with wrong keys in kwargs."""
        s = Square(10, 10, 10, 10)
        s.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(s))


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square to_dictionary method."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_to_dictionary_output(self):
        """Test to_dictionary returns correct output."""
        s = Square(10, 2, 1, 9)
        correct = {"id": 9, "x": 2, "size": 10, "y": 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """Test to_dictionary does not change the object."""
        s1 = Square(10, 2, 1, 9)
        s2 = Square(5, 9, 1, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        """Test to_dictionary with arg."""
        s = Square(10, 2, 4, 1)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
