#!/usr/bin/python3
"""unittest base"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """test cases"""

    def test_NoArg(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, b.id - 1)

    def test_None(self):
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id, b.id - 1)

    def test_three(self):
        a = Base()
        b = Base()
        c = Base()
        self.assertEqual(a.id, c.id - 2)

    def test_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)


class TestJson(unittest.TestCase):
    """test for json"""

    def test_noType(self):
        a = Rectangle(4, 5)
        self.assertEqual(str, type(Base.to_json_string([a.to_dictionary()])))

    def test_none(self):
        self.assertEqual('[]', Base.to_json_string(None))

    def test_empt(self):
        self.assertEqual('[]', Base.to_json_string([]))

    def test_gd(self):
        a = Square(6, 2, 1)
        self.assertEqual('[{"id": 8, "size": 6, "x": 2, "y": 1}]',
                         Base.to_json_string([a.to_dictionary()]))

    def test_em(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_gdi(self):
        a = Rectangle(3, 5, 6, 8, 7)
        Rectangle.save_to_file([a])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(52, len(f.read()))

    def test_man(self):
        a = Square(4, 6, 8)
        b = Square(5, 7, 9)
        c = Square(6, 5, 7)
        d = Square(4, 3, 6)
        Square.save_to_file([a, b, c, d])
        with open("Square.json", 'r') as f:
            self.assertEqual(155, len(f.read()))

    def test_over(self):
        a = Square(6, 9, 9)
        Square.save_to_file([a])
        a = Square(1, 1, 1)
        Square.save_to_file([a])
        with open("Square.json", 'r') as f:
            self.assertEqual(39, len(f.read()))

if __name__ == '__main__':
    unittest.main()
