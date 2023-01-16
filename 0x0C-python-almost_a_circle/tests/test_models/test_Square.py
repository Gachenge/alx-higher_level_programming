#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""unittests for the square"""


class TestCaseSquare(unittest.TestCase):

    def test_isBase(self):
        self.assertIsInstance(Square(6), Base)

    def test_isRect(self):
        self.assertIsInstance(Square(6), Rectangle)

    def test_noArg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_inf(self):
        with self.assertRaises(TypeError):
            Square(float('inf'))

    def test_nan(self):
        with self.assertRaises(TypeError):
            Square(float('nan'))

    def test_negSize(self):
        with self.assertRaises(ValueError):
            Square(-9)

    def test_nx(self):
        with self.assertRaises(ValueError):
            Square(5, -6, 6)

    def test_ny(self):
        with self.assertRaises(ValueError):
            Square(7, 5, -4)

    def test_arsm(self):
        a = Square(6)
        self.assertEqual(36, a.area())

    def test_arbg(self):
        a = Square(9999999999)
        self.assertEqual(99999999980000000001, a.area())

    def test_zersize(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_infx(self):
        with self.assertRaises(TypeError):
            Square(7, float('inf'), 5)

    def test_nany(self):
        with self.assertRaises(TypeError):
            Square(8, 6, float('nan'))


if __name__ == '__main__':
    unittest.main()
