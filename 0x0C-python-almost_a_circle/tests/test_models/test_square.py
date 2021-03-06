#!/usr/bin/python3
"""Unittest for a circle project"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_square(unittest.TestCase):
    """Class Test for square models"""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square(self):
        self.assertTrue(True)

    def test_id(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
        s2 = Square(3, 1, 3, 12)
        self.assertEqual(s2.id, 12)

    def test_setters(self):
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, 2.5)
        self.assertRaises(TypeError, Square, [2, 5])
        self.assertRaises(TypeError, Square, (2, 5))
        self.assertRaises(TypeError, Square, 10, 8, "3")
        self.assertRaises(TypeError, Square, 10, 3.5, 3)
        self.assertRaises(TypeError, Square, 1, 2, 3, 4, 5, 6)
        self.assertRaises(TypeError, Square)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -10)
        self.assertRaises(ValueError, Square, 10, -3, 0)
        self.assertRaises(ValueError, Square, 10, 3, -10)
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        s.x = 3
        self.assertEqual(s.x, 3)
        s.y = 5
        self.assertEqual(s.y, 5)

    def test_area(self):
        s1 = Square(10)
        self.assertEqual(s1.area(), 100)
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_display(self):
        output = io.StringIO()
        sys.stdout = output
        Square(2).display()
        self.assertEqual(output.getvalue(), "##\n##\n")
        output = io.StringIO()
        sys.stdout = output
        Square(2, 1, 1).display()
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    def test_str(self):
        output = io.StringIO()
        sys.stdout = output
        print(Square(4, 2, 1, 12))
        self.assertEqual(output.getvalue(), "[Square] (12) 2/1 - 4\n")
        output = io.StringIO()
        sys.stdout = output
        print(Square(5, 1))
        self.assertEqual(output.getvalue(), "[Square] (1) 1/0 - 5\n")

    def test_update(self):
        s1 = Square(10, 10, 10)
        s1.update(89, 2, 4, 5)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 89)
        s1.update(x=1, size=2, y=3)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 3)

    def test_to_dictionary(self):
        s1_dict = Square(10, 1, 9).to_dictionary()
        dic2 = {'x': 1, 'y': 9, 'id': 1, 'size': 10}
        for key, value in s1_dict.items():
            self.assertEqual(value, dic2[key])
        s1_dict = Square(2, 0, 0, 99).to_dictionary()
        dic2 = {'x': 0, 'y': 0, 'id': 99, 'size': 2}
        for key, value in s1_dict.items():
            self.assertEqual(value, dic2[key])

    def test_inheritance(self):
        s1 = Square(7)
        self.assertEqual(True, isinstance(s1, Base))
        self.assertEqual(True, isinstance(s1, Rectangle))


if __name__ == '__main__':
    unittest.main()
