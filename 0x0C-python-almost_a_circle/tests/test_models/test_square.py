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

class TestOthe(unittest.TestCase):
    """other tests"""

    def test_sqtw(self):
        a = Square(1, 2)
        self.assertEqual(1, a.area())

    def test_frag(self):
        a = Square(1, 2, 3, 4)
        self.assertEqual(4, a.id)

    def test_updt(self):
        a = Square(5, 4, 3, 6)
        a.update()
        self.assertEqual(6, a.id)

    def test_updt1(self):
        a = Square(6, 7, 8, 9)
        a.update(89)
        self.assertEqual(89, a.id)

    def test_updt2(self):
        a = Square(1, 2, 3, 4)
        a.update(89, 6)
        self.assertEqual(6, a.size)

    def test_updt3(self):
        a = Square(1, 2, 3, 4)
        a.update(89, 1, 5)
        self.assertEqual(5, a.x)

    def test_updt4(self):
        a = Square(1, 2, 3, 4)
        a.update(7, 8, 9, 10)
        self.assertEqual(10, a.y)

    def test_upd(self):
        a = Square(4, 5, 6, 7)
        a.update(**{'id': 9})
        self.assertEqual(9, a.id)

    def test_upd1(self):
        a = Square(5, 6, 7, 8)
        a.update(**{'id': 3, 'size': 4})
        self.assertEqual(16, a.area())

    def test_upd2(self):
        a = Square(1, 2, 3, 4)
        a.update(**{'id': 5, 'size': 6, 'x': 7})
        self.assertEqual(7, a.x)

    def test_upd3(self):
        a = Square(1, 2, 3, 4)
        a.update(**{'id': 5, 'size': 6, 'x': 7, 'y': 8})
        self.assertEqual(8, a.y)

    def test_crt(self):
        a = Square.create(**{'id': 4})
        self.assertEqual(4, a.id)

    def test_crt1(self):
        a = Square.create(**{'id': 5, 'size': 8})
        self.assertEqual(64, a.area())

    def test_crt2(self):
        a = Square.create(**{'id': 7, 'size': 9, 'x': 8})
        self.assertEqual(8, a.x)

    def test_crt3(self):
        a = Square.create(**{'id': 1, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(4, a.y)

    def test_crt4(self):
        with self.assertRaises(TypeError):
            Square.create({})

    def test_ldfil(self):
        with self.assertRaises(TypeError):
            Square.load_from_file([], 1)

    def test_string(self):
        a = Square(7)
        self.assertEqual('[Square] ({}) 0/0 - {}'.format(a.id, a.size), str(a))


if __name__ == '__main__':
    unittest.main()
