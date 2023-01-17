#!/usr/bin/python3
"""unittest rectangle"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """test cases rectangle instantiation"""

    def test_noArg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_oneArg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_two(self):
        a = Rectangle(6, 4)
        b = Rectangle(9, 5)
        self.assertEqual(a.id, b.id - 1)

    def test_insta(self):
        self.assertIsInstance(Rectangle(7, 5), Base)


class TestWidthHeight(unittest.TestCase):
    """test cases rectangle width"""

    def test_width(self):
        with self.assertRaises(ValueError):
            Rectangle(6, 0)

    def test_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(-2, 6)

    def test_nan(self):
        with self.assertRaises(TypeError):
            Rectangle(float('nan'), 5)

    def test_inf(self):
        with self.assertRaises(TypeError):
            Rectangle(8, float('inf'))

    def test_int(self):
        with self.assertRaises(TypeError):
            Rectangle('wfsdf', 4)

    def test_xneg(self):
        with self.assertRaises(ValueError):
            Rectangle(7, 5, -3, 7)

    def test_yneg(self):
        with self.assertRaises(ValueError):
            Rectangle(4, 8, 2, -6)

    def test_xnan(self):
        with self.assertRaises(TypeError):
            Rectangle(7, 5, float('nan'), 5)

    def test_yinf(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 3, 5, float('inf'))


class TestArea(unittest.TestCase):
    """test cases for the area"""

    def test_area(self):
        a = Rectangle(3, 2)
        self.assertEqual(6, a.area())

    def test_big(self):
        a = Rectangle(8999999999, 9999999999)
        self.assertEqual(89999999981000000001, a.area())


class TestOther(unittest.TestCase):
    """test everything else"""

    def test_simp(self):
        a = Rectangle(1, 2)
        self.assertEqual(2, a.area())

    def test_thrArg(self):
        a = Rectangle(1, 2, 3)
        self.assertIsInstance(a, Base)

    def test_fouArg(self):
        a = Rectangle(1, 2, 3, 4)
        self.assertIsInstance(a, Base)

    def test_fivArg(self):
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertIsInstance(a, Base)

    def test_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zer(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_stringRep(self):
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual('[Rectangle] (5) 3/4 - 1/2', str(a))


if __name__ == '__main__':
    unittest.main()
